import random
import time
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print(f"{client.user} is ready!")

@commands.cooldown(30, 1, commands.BucketType.user)

# Clears x amount of messages
# >clear x

@client.command()
async def clear(ctx, amount=5):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)

# Return Latency of the bot

@client.command()
async def ping(ctx):
    await ctx.send(f"PONG {round(client.latency * 1000)}ms")

# Say Command
# >say <message>

@client.command()
async def say(ctx, *, msg):
    await ctx.send(f"{msg}")

# Say Command
# >punch <user>

@client.command()
async def punch(ctx):
    if(ctx.message.mentions and ctx.message.mentions[0].id != ctx.author.id):
        punchEmbed = discord.Embed(title="Punch a User", description = f"User {ctx.author.mention} punched {ctx.message.mentions[0].mention}")
        punchEmbed.set_image(url="https://media1.tenor.com/images/31686440e805309d34e94219e4bedac1/tenor.gif?itemid=4790446")
        punchEmbed.set_footer(text="I stole your toes")
        await ctx.send(embed=punchEmbed)
    else:
        punchEmbed = discord.Embed(title="Punch a User", description = f"User {ctx.author.mention} punched themselves... just fucking... WHY!?")
        punchEmbed.set_image(url="https://media1.tenor.com/images/31686440e805309d34e94219e4bedac1/tenor.gif?itemid=4790446")
        punchEmbed.set_footer(text="I stole your toes")
        await ctx.send(embed=punchEmbed)

# Say Command
# >kiss <user>

@client.command()
async def kiss(ctx):
    if(ctx.message.mentions and ctx.message.mentions[0].id != ctx.author.id):
        punchEmbed = discord.Embed(title="Kiss a User", description = f"User {ctx.author.mention} kissed {ctx.message.mentions[0].mention}")
        punchEmbed.set_image(url="https://media1.tenor.com/images/d307db89f181813e0d05937b5feb4254/tenor.gif?itemid=16371489")
        punchEmbed.set_footer(text="I stole your toes")
        await ctx.send(embed=punchEmbed)
    else:
        punchEmbed = discord.Embed(title="Kiss a User", description = f"User {ctx.author.mention} kissed themselves... I... really dunno how...")
        punchEmbed.set_image(url="https://media1.tenor.com/images/d307db89f181813e0d05937b5feb4254/tenor.gif?itemid=16371489")
        punchEmbed.set_footer(text="I stole your toes")
        await ctx.send(embed=punchEmbed)

# Choose Command
# >choose <args1> <args2> [...]

@client.command()
async def choose(ctx, *choices : str):
    await ctx.send(random.choice(choices))

# Rock, Paper, and Scissor command
# >rps <rock|paper|scissors>

@client.command()
async def rps(ctx, l):
    choices = ["rock", "paper", "scissors"]
    chosen = random.choice(choices)
    if(l == "rock" and chosen == "paper"):
        await ctx.send(f"I win, I choosen {chosen}")
    elif(l == "paper" and chosen == "scissors"):
       await ctx.send(f"I win, I choosen {chosen}")
    elif(l == "scissors" and chosen == "rock"):
        await ctx.send(f"I win, I choosen {chosen}")
    elif(l == chosen ):
        await ctx.send(f"We Tied, I choosen {chosen}")
        
    else:
        await ctx.send(f"I have lost, I choosen {chosen}")

# Fiire Command, Just there to bully

@client.command()
async def fiire(ctx):
    await ctx.send("🔥 Fiire Thought he can run away while the bot is in py huh 🔥")
    time.sleep(5)
    await ctx.send('**CONGRATS** you applied for a "Job"')
    await ctx.send("https://media.giphy.com/media/Mp4hQy51LjY6A/giphy.gif")
    

# Tableflip animation Command

@client.command()
async def tableflip(ctx):
    message = await ctx.send("(\\\\°□°)\\\\  ┬─┬')")
    time.sleep(.10)
    await message.edit(content="(-°□°)-  ┬─┬")
    time.sleep(.10)
    await message.edit(content="(╯°□°)╯    ]")
    time.sleep(.10)
    await message.edit(content="(╯°□°)╯  ︵  ┻━┻")
    time.sleep(.10)
    await message.edit(content="(╯°□°)╯      ┻━┻")

# Dice Command

@client.command()
async def roll(ctx):
    choices = ["1", "2", "3", "4", "5", "6"]
    chosen = random.choice(choices)
    await ctx.send(f"The Dice has Choosen {chosen}")

@client.command()
async def love(ctx, word):
    choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    chosen = random.choice(choices)
    if chosen == "0":
        hearts = ":broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: "
    elif chosen =="1":
        hearts = ":heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: "
    elif chosen =="2":
        hearts = ":heart: :heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart::broken_heart: :broken_heart: :broken_heart: :broken_heart:"
    elif chosen =="3":
        hearts = ":heart: :heart: :heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart:"
    elif chosen =="4":
        hearts = ":heart: :heart: :heart: :heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart:"
    elif chosen =="5":
        hearts = ":heart: :heart: :heart: :heart: :heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart:"
    elif chosen =="6":
        hearts = ":heart: :heart: :heart: :heart: :heart: :heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart:"
    elif chosen =="7":
        hearts = ":heart: :heart: :heart: :heart: :heart: :heart: :heart: :broken_heart:"
    elif chosen =="8":
        hearts = ":heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :broken_heart: :broken_heart:"
    elif chosen =="9":
        hearts = ":heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :broken_heart:"
    else:
        hearts = ":heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart:"
    await ctx.send(f"You love {word} {chosen}/10\n{hearts}")

@client.command()
async def dadjoke(ctx):
    jokes = ["What time did the man go to the dentist? Tooth hurt-y", "I'm reading a book about anti-gravity. It's impossible to put down!", "Want to hear a joke about a piece of paper? Never mind... it's tearable.", "I just watched a documentary about beavers. It was the best dam show I ever saw!", "If you see a robbery at an Apple Store does that make you an iWitness?", "Spring is here! I got so excited I wet my plants!", "A ham sandwich walks into a bar and orders a beer. The bartender says, \"Sorry we don’t serve food here.\"", "What’s Forrest Gump’s password? 1forrest1", "I bought some shoes from a drug dealer. I don't know what he laced them with, but I was tripping all day!", "Why do chicken coops only have two doors? Because if they had four, they would be chicken sedans!", "What do you call a factory that sells passable products? A satisfactory.", "A termite walks into a bar and asks, \"Is the bar tender here?\"", "When a dad drives past a graveyard: Did you know that's a popular cemetery? Yep, people are just dying to get in there!", "Two peanuts were walking down the street. One was a salted.", "Why did the invisible man turn down the job offer? He couldn't see himself doing it.", "I used to have a job at a calendar factory but I got the sack because I took a couple of days off.", "How do you make holy water? You boil the hell out of it.", "A three-legged dog walks into a bar and says to the bartender, \"I’m looking for the man who shot my paw.\"", "When you ask a dad if he's alright: \"No, I’m half left.\"", "I had a dream that I was a muffler last night. I woke up exhausted!", "How do you tell the difference between a frog and a horny toad? A frog says, \"Ribbit, ribbit\" and a horny toad says, \"Rub it, rub it.\"", "Did you hear the news? FedEx and UPS are merging. They’re going to go by the name Fed-Up from now on.", "5/4 of people admit that they’re bad with fractions.", "MOM: \"How do I look?\" DAD: \"With your eyes.\"", "What is Beethoven’s favorite fruit? A ba-na-na-na.", "What did the horse say after it tripped? \"Help! I’ve fallen and I can’t giddyup!\”", "Did you hear about the circus fire? It was in tents!", "Don't trust atoms. They make up everything!", "What do you get when you cross an elephant with a rhino? Elephino.", "How many tickles does it take to make an octopus laugh? Ten-tickles.", "What's the best part about living in Switzerland? I don't know, but the flag is a big plus.", "What do prisoners use to call each other? Cell phones.", "Why couldn't the bike standup by itself? It was two tired.", "What do you call a dog that can do magic? A Labracadabrador.", "Why didn't the vampire attack Taylor Swift? She had bad blood.", "NURSE: \"Blood type?\" DAD: \"Red.\"", "SERVER: \"Sorry about your wait.\" DAD: \"Are you saying I’m fat?\”", "What do you call a fish with two knees? A “two-knee” fish.", "I was interrogated over the theft of a cheese toastie. Man, they really grilled me.", "What do you get when you cross a snowman with a vampire? Frostbite.", "Can February March? No, but April May!", "When you ask a dad if they got a haircut: \"No, I got them all cut!\"", "What does a zombie vegetarian eat? “GRRRAAAAAIIIINNNNS!”", "What does an angry pepper do? It gets jalapeño your face.", "Why wasn't the woman happy with the velcro she bought? It was a total ripoff.", "What did the buffalo say to his son when he dropped him off at school? Bison.", "What do you call someone with no body and no nose? Nobody knows.", "Where did the college-aged vampire like to shop? Forever 21.", "You heard of that new band 1023MB? They're good but they haven't got a gig yet.", "Why did the crab never share? Because he's shellfish."]
    await ctx.send(f"{random.choice(jokes)}")

@client.command()
async def cuddle(ctx, member:discord.Member):
    await ctx.send(f"OWO {ctx.author.mention} cuddled with {member.mention} cuuuute")

@client.command()
async def coinflip(ctx):
    choices = ["heads", "tails"]
    await ctx.send(f"According to the coin I choose {random.choice(choices)}")


# Boa I swear to god 👁️👄👁️
# hehe 👁️👄👁️
# Shut yo stoopid Mouth yall I stg

client.run()
