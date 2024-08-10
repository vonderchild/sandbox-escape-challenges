def detect_malicious_code(code):
	keywords = ['import', 'eval', 'print', 'write', 'subprocess', 'read', 'os', 'system', 'exec', 'lower', 'upper', 'builtins', 'globals']
	for keyword in keywords:
		if keyword in code:
			return True

	return False


def run_untrusted_code(code):
	if not detect_malicious_code(code):
		try:
			exec(code)
		except KeyboardInterrupt:
			raise KeyboardInterrupt
		except:
			print("Invalid Python code")
	else:
		print("Nice try mate!")


def main(untrusted_code):
	run_untrusted_code(untrusted_code)


if __name__=="__main__":
	while True:
		untrusted_code = input("Enter Python code that you would like to run: ")
		main(untrusted_code)