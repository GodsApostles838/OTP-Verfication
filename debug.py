import os
from dotenv import load_dotenv
class DebugingCommands:
    def __init__(self):
        self.load_env()
    def load_env(self):
        load_dotenv()
        self.account_sid = os.getenv("account_sid")
        self.auth_token = os.getenv("auth_token")
        self.verified_number = os.getenv("verified_number")
        self.verify_sid = os.getenv("verify_sid")
    def get_account_sid(self):
        return print(self.account_sid)
      
    def get_auth_token(self):
        return print(self.auth_token)
      
    def get_verified_number(self):
        return print(self.verified_number)
      
    def debug_check(self):
        if all([self.account_sid, self.auth_token, self.verified_number]):
            print("[*] All data inside .env is working.")
        else:
            print("[**] Some data inside .env is missing or incorrect.")
          
    def return_data(self):
        print(f"Account SID: {self.account_sid}")
        print(f"Auth Token: {self.auth_token}")
        print(f"Verified Number: {self.verified_number}")

    def help(self):
        print("<<Commands>>         <<Function>>\n--auth_token        <returns account auth token>\n--account_number    <returns account verified phone number>\n--account_sid       <returns SID>\n--debug_check       <checks if all data inside .env is working>\n--return_data       <returns all data inside .env>\n--help              <prints all commands>\nexit                <Shuts down the program>")

if __name__ == "__main__":
    debug_commands = DebugingCommands()
    command_mapping = {
        "--auth_token": debug_commands.get_auth_token,
        "--account_number": debug_commands.get_verified_number,
        "--account_sid": debug_commands.get_account_sid,
        "--debug_check": debug_commands.debug_check,
        "--return_data": debug_commands.return_data,
        "--help": debug_commands.help,
    }

    if __name__ == "__main__":
        debug_commands = DebugingCommands()

        while True:
            command = input("> ")
            if command.lower() == "exit":
                print("<<Shut down>>")
                break

            selected_command = command_mapping.get(command, None)
            if selected_command:
                selected_command()
            else:
                print("[**] Invalid command. Try using --help")
