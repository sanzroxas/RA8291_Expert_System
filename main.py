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
        self.decisions = []

    def start(self):
        self.current_step = 0
        print("Welcome to the RA 8291 Compliance Decision System.")
        self.user_role = input("Are you a government employee, official, or employer? (yes/no): ").strip().lower()
        if self.user_role == 'yes':
            self.choose_topic()
        else:
            print("This law pertains to government employees and officials only. Exiting.")

    def choose_topic(self):
        while True:
            print("\nPlease choose a topic to inquire about:")
            for idx, topic in enumerate(self.topics, 1):
                print(f"{idx}: {topic}")
            choice = int(input("Enter the number corresponding to your choice: ")) - 1
            if 0 <= choice < len(self.topics):
                self.current_step = choice
                self.process_topic()
            else:
                print("Invalid choice. Please try again.")

            more_inquiries = input("Do you have more inquiries? (yes/no): ").strip().lower()
            if more_inquiries != 'yes':
                print("\nThank you for using the RA 8291 Compliance Decision System.")
                break

    def process_topic(self):
        if self.current_step == 0:
            self.employer_contribution()
        elif self.current_step == 1:
            self.fraudulent_transactions()
        elif self.current_step == 2:
            self.compliance_with_gsis()
        elif self.current_step == 3:
            self.employee_contributions()
        elif self.current_step == 4:
            self.government_offices()
        elif self.current_step == 5:
            self.board_member_responsibilities()

    def employer_contribution(self):
        responsible = input(
            "Are you responsible for managing or remitting employee contributions to GSIS? (yes/no): ").strip().lower()
        if responsible == 'yes':
            included = input(
                "Have you included GSIS contributions in the annual budget appropriations? (yes/no): ").strip().lower()
            if included == 'no':
                self.decisions.append("Possible Violation: Omitting contributions may incur penalties.")
                self.decisions.append("Penalty: Imprisonment of 6 months to 6 years, and a fine of P3,000 to P6,000.")
                self.show_decision()
                return
            timely_remittance = input(
                "Were contributions remitted on or before the due date? (yes/no): ").strip().lower()
            if timely_remittance == 'no':
                self.decisions.append("Violation Clause: Late remittance incurs administrative sanctions.")
                self.decisions.append(
                    "Penalty: Fine of P5,000 to P20,000, and imprisonment of 6 years and 1 day to 12 years.")
                self.show_decision()
                return
            delayed = input("Has there been a delay of over 30 days for any remittance? (yes/no): ").strip().lower()
            if delayed == 'yes':
                self.decisions.append("Violation Clause: Delays over 30 days incur severe penalties.")
                self.decisions.append(
                    "Penalty: Fine of P10,000 to P20,000, imprisonment of 1 to 5 years, and disqualification from holding public office.")
                self.show_decision()
                return
        self.decisions.append("Compliance with employer obligations.")
        self.show_decision()

    def fraudulent_transactions(self):
        evidence = input(
            "Are there allegations or evidence of fraud, collusion, or falsification in GSIS transactions? (yes/no): ").strip().lower()
        if evidence == 'yes':
            self.decisions.append("Violation Clause: Any involvement in fraud incurs penalties.")
            self.decisions.append("Penalty: Fine of P5,000 to P20,000, imprisonment of 6 years and 1 day to 12 years.")
            self.show_decision()
            return
        unlawful_funds = input("Did anyone unlawfully obtain funds from GSIS? (yes/no): ").strip().lower()
        if unlawful_funds == 'yes':
            self.decisions.append("Violation Clause: Misrepresentation of entitlement incurs severe penalties.")
            self.decisions.append("Penalty: Fine of P5,000 to P20,000, imprisonment of 6 years and 1 day to 12 years.")
            self.show_decision()
            return
        self.decisions.append("Compliance with fraudulent transaction requirements.")
        self.show_decision()

    def compliance_with_gsis(self):
        compliance = input(
            "Are you or your office compliant with all GSIS regulations and contributions? (yes/no): ").strip().lower()
        if compliance == 'no':
            fail_to_comply = input(
                "Have you failed or refused to comply with any GSIS provision? (yes/no): ").strip().lower()
            if fail_to_comply == 'yes':
                self.decisions.append("Violation Clause: Failure to comply incurs penalties.")
                self.decisions.append(
                    "Penalty: Fine of P5,000 to P20,000, imprisonment of 6 years and 1 day to 12 years.")
                self.show_decision()
                return
        self.decisions.append("Compliance confirmed with GSIS regulations.")
        self.show_decision()

    def employee_contributions(self):
        manage_contributions = input("Do you manage or handle employee GSIS contributions? (yes/no): ").strip().lower()
        if manage_contributions == 'yes':
            remittance = input("Have deducted contributions been remitted within 30 days? (yes/no): ").strip().lower()
            if remittance == 'no':
                self.decisions.append("Violation Clause: Non-remittance presumes misappropriation.")
                self.decisions.append("Penalty: Fine of P5,000 to P20,000, and imprisonment for misappropriation.")
                self.show_decision()
                return
            misappropriation = input("Are there indications of misappropriating GSIS funds? (yes/no): ").strip().lower()
            if misappropriation == 'yes':
                self.decisions.append("Violation Clause: Misappropriation of funds incurs severe penalties.")
                self.decisions.append("Penalty: Imprisonment as per Article 217 of the Revised Penal Code.")
                self.show_decision()
                return
        self.decisions.append("Compliance with employee remittance obligations.")
        self.show_decision()

    def government_offices(self):
        involved = input(
            "Are you involved in the collection or remittance of GSIS contributions? (yes/no): ").strip().lower()
        if involved == 'yes':
            delay = input(
                "Has there been a failure or delay in remitting these accounts within 30 days? (yes/no): ").strip().lower()
            if delay == 'yes':
                self.decisions.append("Violation Clause: Delays result in penalties.")
                self.decisions.append("Penalty: Imprisonment of 1 to 5 years, and a fine of P10,000 to P20,000.")
                self.show_decision()
                return
            civil_liability = input(
                "Are civil liabilities applicable for delayed remittance? (yes/no): ").strip().lower()
            if civil_liability == 'yes':
                self.decisions.append("Violation Clause: Officials may be held civilly liable for damages.")
                self.decisions.append("Penalty: Civil liabilities including surcharges and interest.")
                self.show_decision()
                return
        self.decisions.append("Compliance with national office remittance obligations.")
        self.show_decision()

    def board_member_responsibilities(self):
        board_member = input("Are you a member of the GSIS Board? (yes/no): ").strip().lower()
        if board_member == 'yes':
            failure = input(
                "Have there been any failures to meet obligations under Section 41? (yes/no): ").strip().lower()
            if failure == 'yes':
                self.decisions.append("Violation Clause: Non-compliance incurs penalties.")
                self.decisions.append("Penalty: Imprisonment of 6 months to 1 year, fine of P5,000 to P10,000.")
                self.show_decision()
                return
        self.decisions.append("Compliance with GSIS Board responsibilities.")
        self.show_decision()

    def show_decision(self):
        print("\nDecisions/Outcomes:")
        for decision in self.decisions:
            print(f"- {decision}")
        self.decisions.clear()

if __name__ == "__main__":
    decision_tree = DecisionTree()
    decision_tree.start()
