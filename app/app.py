```python
class LoanApplicationSystem:
    def __init__(self):
        self.applicants = {}

    def add_application(self, ssn, application):
        if ssn not in self.applicants:
            self.applicants[ssn] = []
        if application not in self.applicants[ssn]:
            self.applicants[ssn].append(application)
            self.notify_if_multiple_active(ssn)
            return "Application added."
        return "Duplicate application."

    def get_applications(self, ssn):
        return self.applicants.get(ssn, [])

    def manage_application(self, ssn, application_id, status):
        for app in self.applicants.get(ssn, []):
            if app['id'] == application_id:
                app['status'] = status
                return "Application updated."
        return "Application not found."

    def notify_if_multiple_active(self, ssn):
        active_apps = [app for app in self.applicants[ssn] if app['status'] == 'active']
        if len(active_apps) > 1:
            print(f"Notification: Applicant {ssn} has multiple active loan applications.")

# Example usage
system = LoanApplicationSystem()
system.add_application('123-45-6789', {'id': 1, 'status': 'active'})
system.add_application('123-45-6789', {'id': 2, 'status': 'active'})
print(system.get_applications('123-45-6789'))
system.manage_application('123-45-6789', 1, 'approved')
print(system.get_applications('123-45-6789'))
```