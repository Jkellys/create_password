import random

def create_password(length):
	password = ''
	characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-="
	for i in range(length):
		password += random.choice(characters)
	return password

	

def main():
	pass_len = int(input('Enter how long you want your password to be: '))
	password = create_password(pass_len)
	print("Password: " + str(password))

if __name__ == '__main__':
	main()