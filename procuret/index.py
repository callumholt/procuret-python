# Example of retrieving a single prospective payment
from currency import PR_Currency
from prospective_payment import PR_ProspectivePayment


principal = "10000000"  # $1000 as principal amount
supplier_id = "8420495751947705"  # Example Supplier ID
months = 4  # Duration of 6 months

# Correctly getting an instance of PR_Currency for Australian Dollar
currency = PR_Currency.AUD()

response, error = PR_ProspectivePayment.retrieve(principal, supplier_id,
                                                 currency.indexid, months)

print("this is the response:", response)
print("this is the err:", error)
print("this is the principal:", principal)
print("this is the supplier_id:", supplier_id)
print("this is the currency:", currency)
print("this is the currency.indexid:", currency.indexid)

print("this is the months:", months)

if error:
    print(f"Error occurred: {error}")
else:
    print(f"Payment amount: {response.amount} for {response.periods} months")
