#win 1 1 2 1 1 1 1 2 2 1 3 3 3 1 1 1 1 1 1 1 1 
validate=False
def is_end():
	print ('Бажаєте зіграти ще раз?')
	ch = input ('1)так 2)ні\n')
	while ch !='1' and ch!='2':
		print ('Неправильний вибір. Ви вибрали:'+ch)
		print ('Виберіть 1 або 2')
		ch = input ('1)так 2)ні\n')
	if (ch=='2'):
		return exit ()
	else: validate

def wrong_choice (a,b):
	global ch
	ch=input(a+b)
	while ch!='1' and ch!='2':
		print ('Неправильний вибір. Ви вибрали:'+ch)
		print ('Виберіть 1 або 2')
		ch=input(a+b)
		return (ch)
	
while not validate:
	print ('Long ago, in the ancient land of Minnesota, a 13-year-old boy named Thomas'+
	' resigned inside the attic of his grandmother\'s small house. He spent his days studying'+
	' the combat styles of his favorite anime characters in the hopes that one day he may become'+
	' a master of the lost arts.\nOne day, while browsing web, his internet disconnected.'+
	' Lost and deprived of his research, he realizes what he must do. \n')
	ch1='1) Attempt to fix the internet.\n'
	ch2='2) Give up and go outside.\n'
	wrong_choice (ch1,ch2)
	if ch=='2':
		print ('You give up on your terrible lifestyle and make a few friends,'+
			' met a nice girl, start a family, get a well-paying job and live a generally happy life.'+
			'\nBut you never became a ninja, therefore you are a failure.\n Bad End 1/25')
		validate==is_end ()

	if ch=='1':
		print ('Despite all your best efforts, you can’t manage to figure out how to fix your connection issues.'+
			' You decide that your best option is to search for the masters of the craft.')
		ch=input ('1) Find the I.T. guy. \n')
		while(ch!='1'):
			print ('Неправильний вибір. Ви вибрали:'+ch)
			print ('Виберіть 1\n')
			ch=input ('1) Find the I.T. guy. \n')
		if ch=='1':
			print ('You throw on your Minecraft hoodie and a pair of neon shorts, wrap your ninja headband'+
			' tightly around your forehead, and position your Training katana securely on your back behind'+
			' your panda plush backpack. It\'s time to go. you part the sea of empty Mountain Dew cans blocking'+
			' your path, and walk to the front door, overhearing mumbles from your grandmother about how much of'+ 
			' an embarrassment you are.\n You open the front door to be greeted by the blinding beams of the sun,'+
			' the quiet chirping of the birds, and a slight breeze in the mild weather. Your journey begins.')
			ch1='1) Run back inside in order to escape the horrible thought of having to do things. \n'
			ch2='2) Go to the local diner\n'
			wrong_choice (ch1,ch2)
			
			if ch=='1':
				print('You turn around and travel back to the attic, and plop down on your bed. Without the internet,'+
				'you re-watch the shows you’ve already pirated until you realize you’ve been watching TV for 70 years'+ 
				'straight, and your life is about to end.\n Bad End 2/25 ')
				is_end()


				
			elif ch=='2':
				print ('Diners and bars: the two places it seems everybody goes first when searching for a lead.'+
				'You enter the small restaurant, receiving many odd looks from its patrons.'+
				'You sit in an empty seat at the end of the counter.' + 'The waitress give you a look similar'+ 
				'to that of everyone else and asks: \"What can I get you today?\"')
				ch1='1) \"I’m looking for a scholar of the internet.\"\n'
				ch2='2) Stare at her for an awkward amount of time.\n'
				wrong_choice (ch1,ch2)

				if ch=='1':
					print ('\"I don’t think I can help you with that, sir. Is there anything else you could get for you today?\"')
					ch1='1) \"Information\".\n'
					ch2='2) \"A sandwich\"\n'
					wrong_choice (ch1,ch2)
					if ch=='2':
						print('\"I want a sandwich.\" You say in a loud voice.'+ 
					' She gives the order to the chiefs, then continues helping other customers.'+
					' Some time later you’re faced with a delicious BLT and you savor every bite,'+
					' but then quickly realize you didn\'t bring any money with you. You make a break'+
					' for the door and the officer sitting near you follows.\n It’s been 4 years and you\'re'+
					' still on the run. You have a deep nostalgia for your old anime-watching days.\n Bad End 3/25')
						is_end()


					elif ch=='1':
						print('\"I\'m not sure I can help you with that sir,\" she says in a monotone voice.\n \"Oh really?\"'+
					' you ask then slap down 4 moderately uncommon Pokemon cards and a picture of a giraffe.\n'+
					' She sighs \"I think there\'s a computer technician 2 blocks down from here.\" She says, slightly annoyed.\n'+
					' \"Thank you.\" you say as you stand up and leave.\n You\'re going to miss that giraffe, it\'s'+
					' helped you through many tough times, but some sacrifices must be made.')
						ch=input ('1) Continue your adventures. \n')
						while(ch!='1'):
							print ('Неправильний вибір. Ви вибрали:'+ch)
							print ('Виберіть 1\n')
							ch=input ('1) Continue your adventures. \n')
						if ch=='1':
							print ('You proceed down your path to glory. You\'ve gotten about halfway to your destination when you\'re stopped'+
							'by your worst enemy: Richard. Ever since you first moved into this neighborhood, the demon Richard has been harassing you,'+
							'but today, you\'re prepared. Thanks to your research, you\'re finally ready for the fight of your life.\"Well, well, if it'+
							'isn\'t Nutters? Looks like you’re still eating Nutter Butters.\"Richard says.You calmly respond \"Richard, I\'ve been'+
							'looking forward to this day. Throughout the summer I\'ve been training hard in the ancient arts in order to defeat you.\"'+
							'\"Oh really? is that why you have that toy ninja sword?\" he asks. You\'re taken back by his bravery.')
							ch=input ('1) \"Enough rambling, Let the battle begin!\". \n2) Run and never look back.\n'+
								'3) \"This sword was wielded by samurais, not ninjas!\"\n')
							while ch!='1' and ch!='2'and ch!='3':
								print ('Неправильний вибір. Ви вибрали:'+ch)
								print ('Виберіть 1 або 2 або 3')	
								ch=input ('1) \"Enough rambling, Let the battle begin!\". \n2) Run and never look back.\n'+
								'3) \"This sword was wielded by samurais, not ninjas!\"\n')
							if ch=='2':
								print ('You realize just how bad of an idea challenging him was and make a run for it.'+
								' Then you realize just how bad of an idea running was because he’s a fit jock and you’re a chubby nerd.\n Bad End 4/25 ')
								is_end()


							elif ch=='1':
								print ('\"I\'ve had enough talk, let combat commence!\"\n You pull out your wooden'+
								' katana as he dashes towards you. As he\'s running, he pulls back his right arm,'+
								' preparing for a punch.')
								ch1='1) Block the attack. \n'
								ch2='2) Dodge the attack.\n'
								wrong_choice (ch1,ch2)
								
								if ch=='1':
									print ('You position your sword to block this incoming assault.'+
									' He grabs your sword straight out of your hands and breaks it over your head,'+
									' then punches you directly in the gut. You faint from the pain.\n'+
									' You wake up behind a Mcdonalds. You’re not wearing any clothes and don\'t know your own name. \n'+
									' Bad End 5/25 ')
									is_end()
								elif ch=='2':									
									print ('You manage to just barely dodge his fist. He’s open for an attack.'+
										' You swing your weapon and manage to strike him on his stomach.'+
										' You swing again aiming for his head but he catches the sword and is attempting'+
										' to pull it from your hands.')
									ch1='1) Jab him directly in the face. \n'
									ch2='2) Let go of the sword.\n'
									wrong_choice (ch1,ch2)
									ch3=False
									if ch=='1':
										print ('You forcefully thrust your sword at his face'+
										' and accidentally stab his eye out. You stop in complete'+
										' shock of what you’ve done, but then beams of bright light'+
										' poured out of Richard’s skull and it begins to take the form'+
										' of a tall, thin man.\n \"You have given me freedom from'+
										' that cursed shell. What is your deepest desire?\"')
										ch=input ('1)\"I wish to regain my WiFi.\"\n2)\"I wish to be'+
											' a master of the blade.\"\n3)\"I wish I was cool.\"\n4)\"I wish my mother still loved me.\"\n')
										while ch!='1' and ch!='2'and ch!='3'and ch!='4':
											print ('Неправильний вибір. Ви вибрали:'+ch)
											print ('Виберіть 1 або 2 або 3 або 4')	
											ch=input ('1)\"I wish to regain my WiFi.\"\n2)\"I wish to be'+
											' a master of the blade.\"\n3)\"I wish I was cool.\"\n4)\"I wish my mother still loved me.\"\n')
										if ch=='1':
											print ('\"Very well.\" The figure says.The world flashes to white for a fraction of a second'+
												' and once you regain your sight, he\'s gone. You go home to find that your WiFi has been'+
												' reconnected, and at last, you can get back to your furry roleplay.\n You could\'ve wished'+
												' for anything and you chose to fix your WiFi. You are quite possibly most pathetic human to'+
												' have ever lived. Although I guess you completed your original goal, so that’s alright.\n '+
												' Bad End? 6/25' )
											is_end()
										elif ch=='2':
											print ('\"Very well.\" the man says as you\'re blinded by the light. In a sudden burst of'+
												' knowledge, you learn every technique and skill regarding warfare used by the Japanese hundreds'+
												' of years ago.\n For 9 years you\'ve been training for the day you\'ll become a vigilante, and'+
												' today is that day. After you equip your gear, you head to your local bank where a robbery is'+
												' currently taking place.\n You smash through the skylight to jump attack one of the criminals,'+
												' but you miss and splatter the moment you impact the floor.\n Bad End 7/25')
											is_end()
										elif ch=='3':
											print ('\"Very Well.\" you\'re vision turns white as you suddenly realize how to skateboard and'+
												' talk to people. When the light fades you see that you’re surrounded by friends and the most'+
												' popular girl in school is in your arms.\n Sadly, you gave up on your dreams of being a'+
												' samurai-ninja, which is a loss in my books.\n Bad End 8/25 ')
											is_end()
										while ch=='4'and ch3 == False:
											print('\"I apologize. Although my powers are great, and I can bring the even most improbable wishes'+
												' to be true, I can\'t change what\'s impossible.\"')
											ch=input ('1) Back \n')
											while(ch!='1'):
												print ('Неправильний вибір. Ви вибрали:'+ch)
												print ('Виберіть 1\n')
												ch=input ('1) Back \n')
												
									
									elif ch=='2':
										print ('You release the weapon and Richard flies backward, hitting his head'+
										' on the fence behind him.\n \"Looks like the bully-ee has become the bully-er.\"'+
										' You say with pride.\n You pull your katana out of the stiff hands of your unconscious'+
										' foe (Who probably cracked his head open and is possibly dead.)\n This is a proud victory,'+
										' but you must continue moving forward. your anime cannot wait. ')
										ch=input ('1) Onwards! \n')
										while(ch!='1'):
											print ('Неправильний вибір. Ви вибрали:'+ch)
											print ('Виберіть 1\n')
											ch=input ('1) Onwards! \n')
										if ch=='1':
											print ('You continue your quest to the WiFi masters, during your long journey of'+
											' walking down two more streets, you see a wide range of interesting things: '+
											' You saw a homeless man give the little money he had as a gift, you saw a quarter'+
											' of a pizza floating in the pond. That was just about it.\n Eventually, you arrive '+
											' at your destination: Computing Technological Laptops of the Future for America and'+
											' a Few Other Countries as Well. The signs a bit worn down, and the building is far smaller'+
											' than you remember, but it’s still just as great.\n You peer through the large, dirty window'+
											' to see the dusty shelves holding various reused computer parts and manuals. There\'s'+
											' an obese, middle-aged man with a combover and a thick mustache sleeping next to the cash'+
											' register with nobody else around. \n It’s at this moment you realize you don’t have any'+
											' money, and can’t pay. Yet, you keep your composure as you try to think of something.')
											ch=input ('1) Smash the window and steal a manual.'+
												' \n2) Walk through the front door.\n3) Sneak through the front door.\n4) Search for another way to make cash.\n')
											while ch!='1' and ch!='2'and ch!='3'and ch!='4':
												print ('Неправильний вибір. Ви вибрали:'+ch)
												print ('Виберіть 1 або 2 або 3 або 4')	
												ch=input ('1) Smash the window and steal a manual.'+
													' \n2) Walk through the front door.\n3) Sneak through the front door.\n4) Search for another way to make cash.\n')
											if ch=='1':
												print ('You throw a large stone through the window and scream \"Anarchy!\"\n '+
													' You jump through and grab as many books as you can then manage to escape'+
													' the man running the counter.\n This act of vandalism and robbery caused'+
													' a huge chain of events that lead to the fall of the government and the end'+
													'of humanity.\n Bad End 9/25 ')
												is_end()
											elif ch=='2':
												print ('You casually walk through the front door and wake the employee.'+
												' You greet him with a friendly “Hello” and he welcomes you.\n \"Welcome'+
												' to Computing Technological Laptops of the Future for America and a Few'+
												' Other Countries as Well!\" He says in a loud, deep voice. \"How many I serve you today?\" ')
												ch1='1) \"I\'m looking the man who can fix my internet.\" \n'
												ch2='2) Stare at him.\n'
												wrong_choice(ch1,ch2)
												
												if ch=='2':
													print ('You stare at him and he stares back. Your gaze never breaks, you never blink.'+
														' You both forget the lives you once lived and spend the rest of eternity standing'+
														' in this dusty room, locked in place.\n Bad End 14/25')
													is_end()
												elif ch=='1':
													print('\"That would be me. I am that man!\" he shouts. You’re a bit frightened. \"If you'+
													' can pay the price, I\'ll fix your problem.\"')
													ch1='1) \"I don’t have any money.\"  \n'
													ch2='2) \"I don’t need any money.\"\n'
													wrong_choice(ch1,ch2)
													
													if ch=='2':
														print ('\"I don\'t need any money!\"" you say with confidence. you feel as if you\'re\n'+
													' making a statement despite the fact that you have no idea what that would mean.\n'+
													'\"Well, then I don\'t need you!\" He yells as you hurry out of the shop.\n Bad End 13/25')
														is_end ()
													if ch=='1':
														print ('\"Then why did you come to my shop?\" He shouts even louder. ')
														ch=input ('1)\"To find the man who can fix my internet.\" \n')
														while(ch!='1'):
															print ('Неправильний вибір. Ви вибрали:'+ch)
															print ('Виберіть 1\n')
															ch=input ('1)\"To find the man who can fix my internet.\" \n')
														if ch=='1':
															print('\"But you can\'t make me fix the internet if you can’t pay me!\"\n'+
																' He\'s right, you leave the shop in shame and abandon your quest.'+
																' You\'ve been dishonored, you fear ever showing your face here again.\n'+
																' Bad End 12/25 ')
															is_end ()
											elif ch=='3':
												print ('You quietly open the front door and step in. The only sounds that fill the 11x11'+
												' foot space are the quiet taps of your feet and the sound of an old fan from the early 90\'s. ')
												ch=input ('1) Take a manual off the table. '+
												' \n2) Take a manual off the shelf.\n3) Approach the employee. \n4) Wait\n')
												while ch!='1' and ch!='2'and ch!='3'and ch!='4':
													print ('Неправильний вибір. Ви вибрали:'+ch)
													print ('Виберіть 1 або 2 або 3 або 4')	
													ch=input ('1) Take a manual off the table. '+
												' \n2) Take a manual off the shelf.\n3) Approach the employee. \n4) Wait\n')
												if ch=='1':
													print ('You slowly slide the small book atop a plastic table into your bag,'+
												' being careful to not make any noise. You leave the shop you same way you came'+
												' in, without making a peep.\n You hurry home before sunset, being sure not to let'+
												' anybody see the book you’ve stolen (even though none of them would care). When you'+
												' arrive at your house, you sprint up to your room and open the bag to find you took a'+
												' bible.\n This is probably a metaphor for morality, and that\'s cool and all, but now'+
												' it\'s too late for you to go back and you’ll have to go through all the effort of'+
												' returning there tomorrow.\n Moral of the story: always be sure you stole the right'+
												'thing before heading home.\n Bad End 15/25 ')
													is_end ()
												elif ch=='2':
													print ('You slowly pull a book entitled: How to Fix Your Internet when You\'re a Complete'+
												' Loser. Suddenly, the shelf slides open, revealing a hidden passage.\n It\'s too bad that\n'+
												' the shelf made a loud and woke the employee, you would’ve loved exploring that tunnel, but now'+
												' you\'re exploring past memories flashing before your eyes.\n Bad End 16/25 ')
													is_end ()
												elif ch=='3':
													print('You slowly walk towards the cashier. ')
													ch=input ('1) Wake him up. '+
												' \n2) Steal from the register.\n3) Pickpocket him. \n4) SPOOK!\n')
												while ch!='1' and ch!='2'and ch!='3'and ch!='4':
													print ('Неправильний вибір. Ви вибрали:'+ch)
													print ('Виберіть 1 або 2 або 3 або 4')	
													ch=input ('1) Wake him up. '+
												' \n2) Steal from the register.\n3) Pickpocket him. \n4) SPOOK!\n')
												if ch=='1':
													print('You wake him with a kind greeting. a bit embarrassed, he welcomes you.'+
												' \"Welcome to Computing Technological Laptops of the Future for America and a'+
												' Few Other Countries as Well!” He says in a loud, deep voice. \"How many I serve'+
												' you today?\" ')
													ch1='1) \"I\'m looking for somebody capable of fixing my WiFi. \n'
													ch2='2) Stare at him.\n'
													wrong_choice (ch1,ch2)
													if ch=='1':
														print ('\"That would be me. I am that man!\" he shouts. You\'re a bit frightened. \"If you can pay the price,'+
														' I\'ll fix your problem.\" ')
														ch1='1) \"“I don’t have any money.”\"\n'
														ch2='2) \"I don’t need any money.\"\n'
														wrong_choice (ch1,ch2)
														if ch=='1':
															print ('\"Then why did you come to my shop?\" He shouts even louder. ')
															ch=input ('1) \"To find the man who can fix my internet.\" \n')
															while(ch!='1'):
																print ('Неправильний вибір. Ви вибрали:'+ch)
																print ('Виберіть 1\n')
																ch=input ('1) \"To find the man who can fix my internet.\" \n')
															if ch=='1':
																print ('\"But you can\'t make me fix the internet if you can\'t pay me!\"\n'+
															' He\'s right, you leave the shop in shame and abandon your quest. You\'ve'+
															' been dishonored, you fear ever showing your face here again.\n Bad End 12/25 ')
																is_end ()
														elif ch=='2':
															print('\"I don’t need any money!\" you say with confidence.\n you feel as if'+
															' you\'re making a statement despite the fact that you have no idea what that'+
															' would mean.\n \"Well, then I don\'t need you!\" He yells as you hurry out of'+
															' the shop.\n Bad End 13/25 ')
															is_end ()

													elif ch=='2':
														print('You stare at him and he stares back. Your gaze never breaks, you never blink.'+
														' You both forget the lives you once lived and spend the rest of eternity standing in'+
														' this dusty room, locked in place.\n Bad End 14/25 ')
														is_end ()

												elif ch=='2':
													print ('You silently approach the register and open it. It opens with a loud DING that'+
													' woke the employee, but when the drawer popped out it hit him in the face, putting him'+
													' right back to sleep.\n He was later found to have severe brain damage and lost nearly'+
													' all his motor skills and memory.\n Bad End 17/25 ')
													is_end ()

												elif ch=='3':
													print ('You carefully slip your hand into his pocket to grab his wallet, but instead, find a key.'+
														' You\'re sure his wallet is inside his other pocket, but this key could be useful. ')
													ch1='1) Open the door in the back of the room.\n'
													ch2='2) Search his other pocket.\n'
													wrong_choice (ch1,ch2)
													if ch=='1':
														print ('You walk to the ominous steel door behind the counter and insert the key.'+
															' you take a second to question if you truly wish to see what lies beyond the door. ')
														ch=input ('1) Turn the key. \n')
														while(ch!='1'):
															print ('Неправильний вибір. Ви вибрали:'+ch)
															print ('Виберіть 1\n')
															ch=input ('1) Turn the key. \n')
														if ch=='1':
															print ('Your shaking hands anxiously turn the key. Perhaps what\'s inside this room'+
															' is the final piece to your seemingly endless quest. You quickly pull out the key. ')
															ch=input ('1) Open the mysterious door. \n')
															while(ch!='1'):
																print ('Неправильний вибір. Ви вибрали:'+ch)
																print ('Виберіть 1\n')
																ch=input ('1) Open the mysterious door. \n')
															if ch=='1':
																print ('You turn the doorknob. You take one last deep breath then swing open the door'+
																' to see: an alleyway. This was just a backdoor. ')
																ch1='1) Journey outside.\n'
																ch2='2) continue to pickpocket the cashier.\n'
																wrong_choice (ch1,ch2)
																if ch=='1':
																	print('You don\'t really find anything of interest, it\'s just a dirty alleyway. ')
																	ch=input ('1) Just go back to your original plan already! \n')
																	while(ch!='1'):
																		print ('Неправильний вибір. Ви вибрали:'+ch)
																		print ('Виберіть 1\n')
																		ch=input ('1) Just go back to your original plan already! \n')
																	if ch=='1':
																		print('You gently reach your hand into his pocket to find two things: his wallet,'+
																		' and a piece of paper that says: ‘stop Jacob 346271’ While this paper is far more'+
																		' interesting, the wallet is what you need.\n You open his wallet, take a $20, and feel'+
																		' like an absolutely awful person. You place his wallet on the counter (because you’re not'+
																		' going to take another risk). Time to wake him up. ')
																		ch=input ('1) Why did I add this as an option when there\'s only one choice? I mean, these'+
																		' buttons are where you’re suppose to add options, but if there’s only one button, what’s'+
																		' the point? \n')
																		while(ch!='1'):
																			print ('Неправильний вибір. Ви вибрали:'+ch)
																			print ('Виберіть 1\n')
																			ch=input ('1) Why did I add this as an option when there\'s only one choice? I mean, these'+
																		' buttons are where you’re suppose to add options, but if there’s only one button, what’s'+
																		' the point? \n')
																		if ch=='1':
																			print ('You give him a tap on the shoulder and he jumps up almost instantly. “Hello?”'+
																			' You ask as if you weren’t sneaking around the store for the last 15 minutes.\n“Hello,'+
																			' my name is Nutters, welcome to Computing Technological Laptops of the Future for America'+
																			' and a Few Other Countries as Well! How can I help you today?” He shouts.\n “I’ve been'+
																			' searching far and wide for a scholar of the art’s of connectivity.” You reply.\n “You mean'+
																			' you need somebody to fix your internet connection?” He asks maintaining the same volume.\n'+
																			' “Yeah, I guess that works too...”\n “Alright, it’s $15 upfront.”\n You take out your (or his)'+
																			' shame-fulled $20 and hand it to him. “Thanks, kid!” He says while not giving you the change.'+
																			' “I’ll drive us to your hou- wait! I forgot! I sold my car to pay for that bookshelf!” He says'+
																			' will pointing to an oddly placed shelf.\n “Is your house far away?”\n “Yes, about 2 blocks'+
																			' from here.”\n “That’s a long ways, but I’ve taken further journeys.” He stands atop the table,'+
																			' “And I, Nutters, will travel all across these lands in order to reconnect you with the world!”\n'+
																			' As you both step through the door, you saw the orange sky behind the setting sun. Night was slowly'+
																			' descending upon the city.\n “Alright, which way do we go first?” Nutters asks.\n “West.”\n The duo'+
																			' moves fast along the progressively darkening world. Nightfall was dangerous for Thomas, the shadows'+
																			' gave opportunities for incoming assaults, and it was also past his bedtime. Nightfall was dangerous'+
																			' for Nutters because he had an irrational fear of being outside in the dark.\n Speaking of the darkness,'+
																			' you began seeing strange figures appear around you. Obviously, when you saw these you were off put,'+
																			' but nothing too serious. ')
																			ch=input ('1) Continue.\n')
																			while(ch!='1'):
																				print ('Неправильний вибір. Ви вибрали:'+ch)
																				print ('Виберіть 1\n')
																				ch=input ('1) Continue.\n')
																			if ch=='1':
																				print ('You were making good progress when you heard a loud “Hey!” come from behind you, and you'+
																				' both turned to see a horrifying sight.\n 5 power rangers, each wearing their own $7 Halloween'+
																				' costume surrounded a shadowy figure. He spoke with a nasally voice.\n “Well, well, well, if it'+
																				' isn’t Nutters. You still owe me protection money.”\n Nutters froze, he wasted all his cash on a'+
																				' secret staircase and gasoline canisters.\n “Listen, I don’t have the money yet but-”\n “but I gave'+
																				' you 3 extra days to gather it.” he interupted.\n You were terrified, but Nutters was even more'+
																				' terrified.\n “Do I have to deal with you like I did to Greg?” Mysterious man asks.\n Nutters stays'+
																				' silent, paralyzed by fear. The voice responds to this silence with two words that sent chills down'+
																				' your spine: “Very well.”\n The figure steps from the darkness to reveal the acne ridden face of'+
																				' a pale young-adult man. His brown hair is styled into a short bowl cut and greasy to a point where'+
																				' it looks wet. He’s wearing a high-quality Shadow the Hedgehog costume, for the perfect blend of edge'+
																				' and speed. He’s the type of guy that every man wants to be and every girl wants to be with. ')
																				ch1='1) “Who are you?”\n'
																				ch2='2) The first strike means victory! \n'
																				wrong_choice (ch1,ch2)
																				if ch=='2':
																					print ('You unsheathe your weapon and dash at him. He and his goons take you down with almost no effort.'+
																						' You’re an idiot. Bad End 19/25 ')
																					is_end ()
																				if ch=='1':
																					print ('Гра не дописана. Тому будемо вважати що це перемога.')
																					print ('Win!'*30)
																				exit()


 
				elif ch=='2':
					print ('You give her a blank stare and she gives one back.'+
					'For a straight minute, the only thing the two of you do is gaze into each other\'s eyes.'+
					'You take the time to notice just how pretty she is and she takes the time to notice that you'+
					'probably haven\'t seen a girl in months.\nIt\'s when a drop of drool falls from your chin that'+
					'she breaks the gaze and she leaves without saying a word.\nA while later she returns after serving'+
					'some other customers and asks \"Have you made your choice yet?\"')
					ch1='1) \"Tell me where I can find the I.T. guy\"\n'
					ch2='2) \"A sandwich.\"\n'
					wrong_choice(ch1,ch2)
			
					if ch=='1':
						print ('\"I\'m not sure I can help you with that sir,\" she says in a monotone voice.'+
						'\"Oh really?\"" you ask then slap down 4 moderately uncommon Pokemon cards and a picture of a giraffe.'+
						'She sighs \"I think there\'s a computer technician 2 blocks down from here.\" She says, slightly annoyed.'+
						'\"Thank you.\" you say as you stand up and leave.'+
						'You\'re going to miss that giraffe, it\'s helped you through many tough times, but some sacrifices must be made.')
						ch=input('1) Continue your adventures.\n')
						while ch!='1':
							print ('Неправильний вибір. Ви вибрали:'+ch)
							print ('Виберіть 1')
							ch=input('1) Continue your adventures.\n')
						if (ch=='1'):
							print ('You proceed down your path to glory. You\'ve gotten about halfway to your destination when you\'re stopped'+
							'by your worst enemy: Richard. Ever since you first moved into this neighborhood, the demon Richard has been harassing you,'+
							'but today, you\'re prepared. Thanks to your research, you\'re finally ready for the fight of your life.\"Well, well, if it'+
							'isn\'t Nutters? Looks like you’re still eating Nutter Butters.\"Richard says.You calmly respond \"Richard, I\'ve been'+
							'looking forward to this day. Throughout the summer I\'ve been training hard in the ancient arts in order to defeat you.\"'+
							'\"Oh really? is that why you have that toy ninja sword?\" he asks. You\'re taken back by his bravery.')
					elif ch=='2':
						print ('\"I want a sandwich.\" You say in a loud voice.'+ 
						'She gives the order to the chiefs, then continues helping other customers.'+
						'Some time later you’re faced with a delicious BLT and you savor every bite,'+
						'but then quickly realize you didn\'t bring any money with you.'+
						'You make a break for the door and the officer sitting near you follows.'+
						'It\'s been 4 years and you\'re still on the run.'+
						'You have a deep nostalgia for your old anime-watching days.'+
						'Bad End 3/25 ')
						is_end()

						