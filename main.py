class DecisionTree:
    def __init__(self):
        self.current_step = 0
        self.user_role = None
        self.topics = [
            "Employer Contribution and Budgeting Obligations",
            "Fraudulent and Misleading Transactions",
            "Compliance with GSIS Regulations",
            "Employee Contributions and Remittance Delays",
            "Government Offices and National Compliance",
            "Board Member Responsibilities"
        ]
        self.compliance_result = []
        self.step_function = self.start
        self.compliance_reached = False

    def start(self):
        self.current_step = 0
        return "Welcome to the RA 8291 Compliance Decision System. Are you a government employee, official, or employer?"

    def next_step(self, response):
        if self.step_function == self.start:
            if response.lower() == 'yes':
                self.step_function = self.choose_topic
                return self.choose_topic()
            else:
                return "This law pertains to government employees and officials only. Exiting."
        elif self.step_function == self.choose_topic:
            return self.choose_topic(response)
        elif self.step_function:
            return self.step_function(response)

    def choose_topic(self, topic_name=None):
        if topic_name is None:
            options = "\n".join(self.topics)
            return f"Please choose a topic to inquire about:\n{options}"
        if topic_name in self.topics:
            topic_idx = self.topics.index(topic_name)
            self.current_step = topic_idx
            topic_functions = [
                self.employer_contribution,
                self.fraudulent_transactions,
                self.compliance_with_gsis,
                self.employee_contributions,
                self.government_offices,
                self.board_member_responsibilities
            ]
            self.step_function = topic_functions[topic_idx]
            return topic_functions[topic_idx]()
        else:
            return "Invalid choice. Please try again."

    def employer_contribution(self, response=None):
        if response is None:
            return "Are you responsible for managing or remitting employee contributions to GSIS?"
        if response == 'yes':
            self.step_function = self.employer_contribution_included
            return "Have you included GSIS contributions in the annual budget appropriations?"
        self.compliance_result.append("This topic might not be relevant to you.")  # Updated here
        return self.show_compliance_result()  # Update this call

    def employer_contribution_included(self, response):
        if response == 'no':
            self.compliance_result.append("Possible Violation: Omitting contributions may incur penalties.")  # Updated here
            self.compliance_result.append("Penalty: Imprisonment of 6 months to 6 years, and a fine of P3,000 to P6,000.")  # Updated here
            return self.show_compliance_result()  # Update this call
        self.step_function = self.employer_contribution_timely
        return "Were contributions remitted on or before the due date?"

    def employer_contribution_timely(self, response):
        if response == 'no':
            self.compliance_result.append("Violation Clause: Late remittance incurs administrative sanctions.")  # Updated here
            self.compliance_result.append("Penalty: Fine of P5,000 to P20,000, and imprisonment of 6 years and 1 day to 12 years.")  # Updated here
            return self.show_compliance_result()  # Update this call
        self.step_function = self.employer_contribution_delayed
        return "Has there been a delay of over 30 days for any remittance?"

    def employer_contribution_delayed(self, response):
        if response == 'yes':
            self.compliance_result.append("Violation Clause: Delays over 30 days incur severe penalties.")  # Updated here
            self.compliance_result.append("Penalty: Fine of P10,000 to P20,000, imprisonment of 1 to 5 years, and disqualification from holding public office.")  # Updated here
            return self.show_compliance_result()  # Update this call
        self.compliance_result.append("Compliance with employer obligations.")  # Updated here
        return self.show_compliance_result()  # Update this call

    def fraudulent_transactions(self, response=None):
        if response is None:
            return "Are there allegations or evidence of fraud, collusion, or falsification in GSIS transactions?"
        if response == 'yes':
            self.compliance_result.append("Violation Clause: Any involvement in fraud incurs penalties.")  # Updated here
            self.compliance_result.append("Penalty: Fine of P5,000 to P20,000, imprisonment of 6 years and 1 day to 12 years.")  # Updated here
            return self.show_compliance_result()  # Update this call
        self.step_function = self.fraudulent_transactions_unlawful
        return "Did anyone unlawfully obtain funds from GSIS?"

    def fraudulent_transactions_unlawful(self, response):
        if response == 'yes':
            self.compliance_result.append("Violation Clause: Misrepresentation of entitlement incurs severe penalties.")  # Updated here
            self.compliance_result.append("Penalty: Fine of P5,000 to P20,000, imprisonment of 6 years and 1 day to 12 years.")  # Updated here
            return self.show_compliance_result()  # Update this call
        self.compliance_result.append("Compliance with fraudulent transaction requirements.")  # Updated here
        return self.show_compliance_result()  # Update this call

    def compliance_with_gsis(self, response=None):
        if response is None:
            return "Are you or your office compliant with all GSIS regulations and contributions?"
        if response == 'no':
            self.step_function = self.compliance_with_gsis_fail
            return "Have you failed or refused to comply with any GSIS provision?"
        self.compliance_result.append("Compliance confirmed with GSIS regulations.")  # Updated here
        return self.show_compliance_result()  # Update this call

    def compliance_with_gsis_fail(self, response):
        if response == 'yes':
            self.compliance_result.append("Violation Clause: Failure to comply incurs penalties.")  # Updated here
            self.compliance_result.append("Penalty: Fine of P5,000 to P20,000, imprisonment of 6 years and 1 day to 12 years.")  # Updated here
            return self.show_compliance_result()  # Update this call
        self.compliance_result.append("Compliance confirmed with GSIS regulations.")  # Updated here
        return self.show_compliance_result()  # Update this call

    def employee_contributions(self, response=None):
        if response is None:
            return "Do you manage or handle employee GSIS contributions?"
        if response == 'yes':
            self.step_function = self.employee_contributions_remittance
            return "Have deducted contributions been remitted within 30 days?"
        self.compliance_result.append("This topic might not be relevant to you.")  # Updated here
        return self.show_compliance_result()  # Update this call

    def employee_contributions_remittance(self, response):
        if response == 'no':
            self.compliance_result.append("Violation Clause: Non-remittance presumes misappropriation.")  # Updated here
            self.compliance_result.append("Penalty: Fine of P5,000 to P20,000, and imprisonment for misappropriation.")  # Updated here
            return self.show_compliance_result()  # Update this call
        self.step_function = self.employee_contributions_misappropriation
        return "Are there indications of misappropriating GSIS funds?"

    def employee_contributions_misappropriation(self, response):
        if response == 'yes':
            self.compliance_result.append("Violation Clause: Misappropriation of funds incurs severe penalties.")  # Updated here
            self.compliance_result.append("Penalty: Imprisonment as per Article 217 of the Revised Penal Code.")  # Updated here
            return self.show_compliance_result()  # Update this call
        self.compliance_result.append("Compliance with employee remittance obligations.")  # Updated here
        return self.show_compliance_result()  # Update this call

    def government_offices(self, response=None):
        if response is None:
            return "Are you involved in the collection or remittance of GSIS contributions?"
        if response == 'yes':
            self.step_function = self.government_offices_delay
            return "Has there been a failure or delay in remitting these accounts within 30 days?"
        self.compliance_result.append("This topic might not be relevant to you.")  # Updated here
        return self.show_compliance_result()  # Update this call

    def government_offices_delay(self, response):
        if response == 'yes':
            self.compliance_result.append("Violation Clause: Delays result in penalties.")  # Updated here
            self.compliance_result.append("Penalty: Imprisonment of 1 to 5 years, and a fine of P10,000 to P20,000.")  # Updated here
            return self.show_compliance_result()  # Update this call
        self.step_function = self.government_offices_civil_liability
        return "Are civil liabilities applicable for delayed remittance?"

    def government_offices_civil_liability(self, response):
        if response == 'yes':
            self.compliance_result.append("Violation Clause: Civil liabilities apply to late remittances.")  # Updated here
            self.compliance_result.append("Penalty: Administrative fines may apply.")  # Updated here
            return self.show_compliance_result()  # Update this call
        self.compliance_result.append("Compliance with national office remittance obligations.")  # Updated here
        return self.show_compliance_result()  # Update this call

    def board_member_responsibilities(self, response=None):
        if response is None:
            return "Are you serving on the board of trustees for GSIS?"
        if response == 'yes':
            self.step_function = self.board_member_responsibilities_duties
            return "Have you fulfilled your duties to protect member contributions?"
        self.compliance_result.append("This topic might not be relevant to you.") # Updated here
        return self.show_compliance_result()  # Update this call

    def board_member_responsibilities_duties(self, response):
        if response == 'no':
            self.compliance_result.append("Violation Clause: Non-fulfillment of duties incurs penalties.")  # Updated here
            self.compliance_result.append("Penalty: Imprisonment of 6 years to 6 years and 1 day.")  # Updated here
            return self.show_compliance_result()  # Update this call
        self.compliance_result.append("Compliance with board member responsibilities.")  # Updated here
        return self.show_compliance_result()  # Update this call

    def show_compliance_result(self):
        self.compliance_reached = True  # Set the flag when showing compliance results
        return "\n".join(
            self.compliance_result) if self.compliance_result else "No violations detected. Would you like to inquire again?"

    def reset_compliance_state(self):
        self.current_step = 0
        self.user_role = None
        self.compliance_result = []
        self.step_function = self.start
        self.compliance_reached = False

    def to_dict(self):
        return {
            "current_step": self.current_step,
            "user_role": self.user_role,
            "compliance_result": self.compliance_result,
            "step_function": self.step_function.__name__ if self.step_function else None
        }

    @classmethod
    def from_dict(cls, data):
        instance = cls()
        instance.current_step = data['current_step']
        instance.user_role = data.get('user_role')
        instance.compliance_result = data.get('compliance_result', [])
        # Restore the step function based on its name
        step_function_name = data.get('step_function')
        if step_function_name and hasattr(instance, step_function_name):
            instance.step_function = getattr(instance, step_function_name)
        return instance