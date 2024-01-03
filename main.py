import os
from twilio.rest import Client
from dotenv import load_dotenv
class TwilioOTPVerifier:
    def __init__(self, account_sid, auth_token, verify_sid, verified_phone_number):
        self.client = Client(account_sid, auth_token)
        self.verify_sid = verify_sid
        self.verified_phone_number = verified_phone_number
    def send_otp(self):
        verification = self.client.verify.services(self.verify_sid).verifications.create(
            to=self.verified_phone_number, channel="sms"
        )
        print(f"[*] OTP Code sent to {self.verified_phone_number}")
        return verification.status

    def check_otp(self, otp_code):
        verification_check = self.client.verify.services(self.verify_sid).verification_checks.create(
            to=self.verified_phone_number, code=otp_code
        )
        return verification_check

def main():
    # Load 
    load_dotenv()

    # Credientials
    account_sid = os.getenv("account_sid")
    auth_token = os.getenv("auth_token")
    verify_sid = os.getenv("verify_sid")
    verified_phone_number = os.getenv("verified_number")

    # Verify
    otp_verifier = TwilioOTPVerifier(account_sid, auth_token, verify_sid, verified_phone_number)

    # Send OTP and get verification status
    otp_status = otp_verifier.send_otp()
    print(f"OTP Status: {otp_status}")

    # Input OTP code from the user
    otp_code = input("Enter the OTP code sent to your number: ")

    # Check OTP and get verification result
    otp_verification_result = otp_verifier.check_otp(otp_code)
    print("[*] Verification Result:", otp_verification_result.status)

if __name__ == "__main__":
    main()
