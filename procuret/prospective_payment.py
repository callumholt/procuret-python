# A theoretical payment amount, and the number of months over which that
# payment would be made, if a customer successfully applied for a Procuret
# Instalment Plan

import requests
from currency import PR_Currency


class PR_ProspectivePayment:

    @staticmethod
    def path():
        return 'https://procuret.com/api/credit/prospective-payment'

    @staticmethod
    def list_path():
        return PR_ProspectivePayment.path() + '/list'

    def __init__(self, payment, raw_cycle, supplier_id, periods, currency):
        self._payment = payment
        self._raw_cycle = raw_cycle
        self._supplier_id = supplier_id
        self._periods = periods
        self._currency = currency

    @property
    def periods(self):
        return self._periods

    @property
    def amount(self):
        return PR_Amount(self._payment, self._currency)

    @property
    def supplier_id(self):
        return self._supplier_id

    @staticmethod
    def decode(data):
        # Assuming PR_Currency has a decode method implemented
        return PR_ProspectivePayment(data['payment'], data['cycle'],
                                     data['supplier_id'], data['periods'],
                                     PR_Currency.decode(data['currency']))

    @staticmethod
    def retrieve(principal,
                 supplier_id,
                 denomination,
                 months,
                 endpoint=None,
                 session=None):
        try:
            # Construct the URL
            url = PR_ProspectivePayment.path() if endpoint is None else endpoint

            # Construct query parameters
            params = {
                'cycle': 1,
                'supplier_id': supplier_id,
                'principle': principal,
                'periods': months,
                'denomination': denomination
            }
            print("Sending API request with params:", params)

            # Make the GET request
            response = requests.get(url, params=params)

            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()
                return PR_ProspectivePayment.decode(data), None
            else:
                error_message = f"Failed to retrieve data. Status code:{
                    response.status_code}, Response: {response.text}"

                return None, error_message

        except Exception as error:
            return None, error


@staticmethod
def retrieve_all_available(principal,
                           denomination,
                           supplier_id,
                           endpoint=None,
                           session=None):
    try:
        targets = [
            PR_QueryTerm('cycle', 1),
            PR_QueryTerm('supplier_id', supplier_id),
            PR_QueryTerm('principal_magnitude', principal),
            PR_QueryTerm('denomination', denomination.indexid)
        ]

        parameters = PR_QueryString(targets)
        # Implement the API request here
        # response = your_api_request_function(PR_ProspectivePayment.list_path(), parameters)

        # Process the response
        # Assuming a function to handle the response
        # return handle_response(response)

    except Exception as error:
        # Handle error
        return None, error


# Placeholders for other classes


class PR_Amount:

    def __init__(self, payment, currency):
        self.payment = payment
        self.currency = currency

    def __str__(self):
        # This method defines how the amount is represented as a string.
        # You can customize it based on how you want to format the amount and currency.
        return f"{self.currency.symbol}{self.payment}"


class PR_QueryTerm:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class PR_QueryString:

    def __init__(self, query_terms):
        # Assuming query_terms is a list of PR_QueryTerm objects
        self.query_terms = query_terms
        # Implement any additional logic needed to construct the query string

    # Additional methods as required for your implementation


# Example usage -> DELETE BEFORE PULL REQUEST
# response, error = PR_ProspectivePayment.retrieve('600', '511291212', PR_Currency.AUD, 12)
'''
# Example of retrieving a single prospective payment
principal = "1000"  # $1000 as principal amount
supplier_id = "123456789"  # Example Supplier ID
currency = PR_Currency.AUD  # Assuming PR_Currency.AUD is a valid currency object
months = 6  # Duration of 6 months

response, error = PR_ProspectivePayment.retrieve(principal, supplier_id, currency, months)
if error:
    print(f"Error occurred: {error}")
else:
    print(f"Payment amount: {response.amount} for {response.periods} months")


'''
'''
# Example of retrieving all available prospective payments
principal = "5000"  # $5000 as principal amount
supplier_id = "987654321"  # Another Example Supplier ID
currency = PR_Currency.USD  # Assuming PR_Currency.USD is a valid currency object

payments, error = PR_ProspectivePayment.retrieve_all_available(principal, currency, supplier_id)
if error:
    print(f"Error occurred: {error}")
else:
    for payment in payments:
        print(f"Payment option: {payment.amount} per month for {payment.periods} months")

'''
