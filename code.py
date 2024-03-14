import subprocess

api_key = "xKoANqqzawj7WG3CDfROZUxV3qKQXDN3" #API key
curl_command = f'curl -H "X-Dune-API-Key:{api_key}" "https://api.dune.com/api/v1/query/3520819/results/csv?limit=10000"'

result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

if result.returncode == 0:
    # Write the output to a CSV file
    with open("query_result.csv", "w") as file:
        file.write(result.stdout)
        print("CSV data has been saved to query_result.csv")
else:
    print("Failed to retrieve CSV data:", result.stderr)
