import secrets
from flask import Flask, render_template, request, redirect, session
from main import DecisionTree

app = Flask(__name__)
secret_key = secrets.token_hex(16)
app.secret_key = secret_key

@app.before_request
def init_tree():
    if 'tree' not in session:
        session['tree'] = DecisionTree().to_dict()

@app.route('/')
def index():
    tree_data = session.get('tree')
    tree = DecisionTree.from_dict(tree_data)
    question = tree.start()
    session['tree'] = tree.to_dict()
    return render_template('index.html', question=question)

@app.route('/decision', methods=['POST'])
def decision():
    tree_data = session.get('tree')
    tree = DecisionTree.from_dict(tree_data)
    response = request.form['response']

    # Handling initial question about being a government employee
    if tree.step_function == tree.start:
        if response.lower() == 'yes':
            # Direct to topic selection
            tree.step_function = tree.choose_topic  # Set the step function
            question = "Please choose a topic to inquire about:"
        else:
            # Update the message to ask if they want to inquire anyway
            question = "This law pertains to government employees and officials only. Would you like to inquire anyway?"
            session['tree'] = tree.to_dict()  # Update the session state
            tree.step_function = tree.show_compliance_result  # Set the step function for the next interaction

    # Handle follow-up response about using the compliance checker
    elif tree.step_function == tree.show_compliance_result:
        if response.lower() == 'yes':
            tree.step_function = tree.choose_topic  # Proceed to choose topic
            question = "Please choose a topic to inquire about:"  # Updated to remove the topic list
        else:
            # Direct to a goodbye page when they choose No
            return render_template('goodbye.html', message="Thanks for using our RA 8291 Compliance Checker. Remember that this does not constitute as legal advice")

    else:
        # Continue with decision-making process
        question = tree.next_step(response)

    # Update session with the current state
    session['tree'] = tree.to_dict()

    # Check if a compliance result has been reached
    if tree.compliance_reached:
        compliance_result = tree.show_compliance_result()
        return render_template('index.html', compliance_result=compliance_result)

    return render_template('index.html', question=question)


@app.route('/reset', methods=['POST'])
def reset():
    tree_data = session.get('tree')
    tree = DecisionTree.from_dict(tree_data)
    tree.reset_compliance_state()
    response = request.form['response']

    # Handling initial question about being a government employee
    if tree.step_function == tree.choose_topic:
        question = "Please choose a topic to inquire about:"

    # Handle follow-up response about using the compliance checker
    elif tree.step_function == tree.show_compliance_result:
        if response.lower() == 'yes':
            tree.step_function = tree.choose_topic  # Proceed to choose topic
            question = tree.choose_topic()  # Call choose_topic function
        else:
            return render_template('index.html', message="Thanks for using our RA 8291 Compliance Checker. Remember that this does not constitute as legal advice")

    # Check if the user wants to inquire again after showing compliance results
    elif response.lower() == 'another_inquiry':
        current_topic = session.get('current_topic', "Please choose a topic to inquire about:")
        question = current_topic  # Direct back to the last topic
        tree.step_function = tree.choose_topic  # Reset to choose topic step

    else:
        # Continue with decision-making process
        question = tree.next_step(response)

    # Update session with the current state
    session['tree'] = tree.to_dict()

    # Check if a compliance result has been reached
    if tree.compliance_reached:
        compliance_result = tree.show_compliance_result()
        return render_template('index.html', compliance_result=compliance_result)

    # Store the current topic in the session
    session['current_topic'] = question if "choose a topic" in question else session.get('current_topic')

    return render_template('index.html', question=question)

@app.route('/done', methods=['POST'])
def done():
    # Logic to handle "Done Inquiring"
    session.clear()
    return render_template('index.html', message="Thanks for using our RA 8291 Compliance Checker. Remember that this does not constitute as legal advice")

if __name__ == "__main__":
    app.run(debug=True)
