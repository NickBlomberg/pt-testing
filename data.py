class Data(object):
    """Data configurations for all test cases"""
    config = {
        "login1": {
            "user": "sharenet.admin@redhat.com",
            "pass": "redhat",
        },

        "login2": {
            "user": "sharenet.admin@redhat.com",
            "pass": "wrong"
        },

        "project1": {
            "salesforce": "001001",
            "region": "DA",
            "country": "Germany",
            "delivery_customer": "QA-TESCO, United Kingdom [5665828]",
            "channel_partner": "Amadeus, Germany [7276922]",
            "pa_number": "1010103",
            "indirect_salesforce": "991199",
            "name": "Selenium Test Project",
            "description": "Test: project description",
            "no_third_party": True,
            "stage": "Current",
            "pt_status": "Active",
            "status_comment": "Test: status comment",
            "main_product": "RHEL",
            "scope": "GPS",
            "revenue_recognition": "Consulting Units",
            "salesperson": "Alexander Picker (DA, Munich)",
            "rsm": "Mark Schulze",
            "sdm": "Eric Lavarde (DA, Stuttgart) [1835157]",
            "pm": "Irena Pribova (Nordics, Stockholm) [2144168]",
            "solution_architect": "Rhys Oxenham (UKIE, Farnborough) [530308]",
            "contract_type": "T&M Hourly",
            "contract_closure": "10 Jul 2016",
            "start_date": "12 Jul 2016",
            "end_date": "11 Jul 2017",
            "contract_currency": "EUR",
            "billable_unit": "Hour",
            "contract_amount": "100",
            "payment_schedule": "monthly",
            "payment_comment": "Test: payment comment"
        },

        "task1": {
            "number": "2",
            "name": "Selenium Test Task",
            "important_information":  "Important Information",
            "delivery_address": "Delivery Address",
            "business_unit": "Cloud",
            "solutions": "Core Build",
            "timesheets_required": True,
            "customer_contact": "John Shepherd <john.shepherd@oup.com>",
            "pm": "Irena Pribova (Nordics, Stockholm) [2144168]",
            "solution_architect": "Rhys Oxenham (UKIE, Farnborough)",
            "units": "99",
            "labour_rate": "100",
            "expense_rate": "20",
            "expenses": "included",
            "expense_conditions": "Expense Conditions",
            "autosync_deliveries": True
        },

        "url": {
            "project_form": "http://localhost:9000/projects-emea/project-edit"
        }
    }