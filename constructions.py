status_map = {
    '201': 'Working',
    '301': 'Error\nPlease refer to status map #1',
    '401': 'Already opened',
    '501': 'Not opening. Try closing the application.'
}

def returnOutput(arg1, status_code):
    status = status_map.get(status_code, 'Unknown')  # Default to 'Unknown' if code is not found
    print("[+]", arg1, status)

# Example call
returnOutput("Status:", '201')
