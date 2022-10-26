# This program is a game for guessing a secret number


secret_number = 13
user_number = int( input( 'Qual número você imagina que tem o presidente que irá ganhar? ' ) )


# Keep asking the number for the user if it isn't the same as the secret_number
while user_number != secret_number: 
	print('ÉRRRR, se liga, hein! Bora tentar de novo? ')
	user_number = int( input( 'Qual número você imagina que tem o presidente que irá ganhar? ' ) )
		

# If the user finally guess the number, print a congratulations message
print( 'Parabénssssss, é isso aí, ja diria Ana Carolina!' )


