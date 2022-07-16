print('''


                       ,sdPBbs.					 (      /|\      .    |      \      .   +      
                      ,d$$$$$$$$b.				     . |||||     _    | |   | | ||         .   
                     d$P'`Y'`Y'`?$b				.      |||||    | |  _| | | | |_||    .        
                    d'    `  '  \ `b				.      |||||    | |  _| | | | |_||    .        
                   /    |        \  \				__||||_|||||____| |_|_____________\__________  
                  /    / \       |   \				. |||| |||||  /\   _____      _____  .   .     
             _,--'        |      \    |				  |||| ||||| ||||   .   .  .         ________  
           /' _/          \   |        \			 . \|`-'|||| ||||    __________       .    .   
        _/' /'             |   \        `-.__			    \__ |||| ||||      .          .     .      
    __/'       ,-'    /    |    |     \      `--...__		  __    ||||`-'|||  .       .    __________    
  /'          /      |    / \     \     `-.           `\	 .    . |||| ___/  ___________             .   
 /    /;;,,__-'      /   /    \            \            `-.	    . _ ||||| . _               .   _________  
/    |;;;;;;;\                                             \ 	 _   ___|||||__  _           .          _      


''')

print('''
      You stand at a crossroads. You see two paths ahead of you through forrests and dessert. You know that only one of them will get you safely to your destination, the other will be your undoing.

Two brothers are standing nearby. One of them is always telling the truth, the other is always lying. You need to ask both of them the same question on the basis of which you will find out which way to go. Remember they are mean, you only get one chance.

What question will you ask?
      
      ''')

ans=input(" > ")

# Which path would your brother choose?

# Which path would your brother choose?
if(ans.strip().lower().replace(' ','')=="whichpatchwouldyourbrotherchoose?"):
  print("Great question, you're great pretender")
else:
  print("Well it didn't went well")
  
# Working url:
# https://replit.com/@KotminPlay/BrotherQuestMiniGame?v=1&embed=1&output=1