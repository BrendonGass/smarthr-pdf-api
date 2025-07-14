from fpdf import FPDF
from datetime import datetime

class SmartHRPDF(FPDF):
    def header(self):
        self.image("smarthr_logo.png", 10, 8, 60)
        self.set_font("Arial", 'B', 14)
        self.ln(25)
        self.cell(200, 10, txt="SmartHR Salary Report", ln=True, align="L")
        self.set_font("Arial", '', 11)
        self.cell(200, 8, txt="Managing the heart of your business", ln=True)
        self.ln(5)

    def add_table(self, rows, col_widths):
        self.set_font("Arial", '', 11)
        for row in rows:
            for i in range(len(row)):
                self.cell(col_widths[i], 8, str(row[i]), border=1)
            self.ln()

    def build(self, data):
        self.add_page()

        # Summary
        self.set_font("Arial", '', 11)
        self.cell(200, 8, txt="Tax Year: 2025/2026", ln=True)
        self.cell(200, 8, txt=f"Name: {data['name']}", ln=True)
        self.cell(200, 8, txt=f"Date Calculated: {datetime.today().strftime('%d %B %Y')}", ln=True)

        self.ln(8)
        self.set_font("Arial", 'B', 12)
        self.cell(200, 10, txt="What You Provided", ln=True)
        inputs = [
            ["Item", "Value"],
            ["Gross Salary", data['gross_salary']],
            ["Age", data['age']],
            ["Travel Allowance", data['travel_allowance']],
            ["Travel Included in Salary", data['travel_included']],
            ["Pension (Employee)", data['pension_employee']],
            ["Pension (Employer)", data['pension_employer']],
            ["Medical Aid Dependants", data['medical_dependants']]
        ]
        self.add_table(inputs, [70, 110])

        self.ln(5)
        self.set_font("Arial", 'B', 12)
        self.cell(200, 10, txt="Deductions and Tax Credits", ln=True)
        deductions = [
            ["Item", "Monthly Amount"],
            ["PAYE", data['paye']],
            ["UIF", data['uif']],
            ["Pension (Employee)", data['pension_employee']],
            ["Medical Aid Credit", data['medical_credit']]
        ]
        self.add_table(deductions, [90, 90])

        self.ln(5)
        self.set_font("Arial", 'B', 12)
        self.cell(190, 10, f"Net Salary: {data['net_pay']} per month", ln=True)

        # Payslip
        self.ln(8)
        self.set_font("Arial", 'B', 12)
        self.cell(200, 10, txt="Sample Payslip (for illustration only)", ln=True)
        payslip = [
            ["Description", "Amount"],
            ["Basic Salary", data['gross_salary']],
            ["Travel Allowance", data['travel_allowance']],
            ["", ""],
            ["PAYE", "-" + data['paye']],
            ["UIF", "-" + data['uif']],
            ["Pension (Employee)", "-" + data['pension_employee']],
            ["", ""],
            ["Net Pay", data['net_pay']]
        ]
        self.add_table(payslip, [95, 95])

        self.ln(4)
        self.set_font("Arial", 'I', 10)
        self.multi_cell(0, 6, "Note: This report is a simulation. For legal payslips, contact your payroll provider.")

