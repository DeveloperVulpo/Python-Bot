import discord
import random
import requests
import asyncio
from discord.ext import commands

class Fun(commands.Cog):
    def __init__ (self, bot): self.bot = bot
    
    # Punch Command
    # >punch <user>
    @commands.command()
    async def punch(self, ctx, user: discord.Member = None):
        if user == ctx.author or user == None:
            punchEmbed = discord.Embed(title = "Punch a User", description = f"User {ctx.author.mention} punched themselves... just fucking... WHY!?")
        else:
            punchEmbed = discord.Embed(title="Punch a User", description = f"User {ctx.author.mention} punched {user.mention}")
        punchEmbed.set_image(url="https://media1.tenor.com/images/31686440e805309d34e94219e4bedac1/tenor.gif?itemid=4790446")
        punchEmbed.set_footer(text="I stole your toes")
        await ctx.send(embed=punchEmbed)

    # Choose Command
    # >choose <args1> <args2> [...]
    @commands.command()
    async def choose(self, ctx, *choices: str):
        await ctx.send(random.choice(choices))

    # Rock, Paper, and Scissor command
    # >rps <rock|paper|scissors>
    @commands.command()
    async def rps(self, ctx, l: str):
        choices = ["rock", "paper", "scissors"]
        chosen = random.choice(choices)

        if l == "rock" and chosen == "paper":
            await ctx.send(f"I win, I chose {chosen}")
        elif l == "paper" and chosen == "scissors":
            await ctx.send(f"I win, I chose {chosen}")
        elif l == "scissors" and chosen == "rock":
            await ctx.send(f"I win, I chose {chosen}")
        elif l == chosen:
            await ctx.send(f"We Tied, I chose {chosen}")
        else:
            await ctx.send(f"I have lost, I chose {chosen}")
    
    # Tableflip animation Command
    # >tableflip
    @commands.command()
    async def tableflip(self, ctx):
        message = await ctx.send("(\\\\°□°)\\\\  ┬─┬')")
        await asyncio.sleep(.10)
        await message.edit(content="(-°□°)-  ┬─┬")
        await asyncio.sleep(.10)
        await message.edit(content="(╯°□°)╯    ]")
        await asyncio.sleep(.10)
        await message.edit(content="(╯°□°)╯  ︵  ┻━┻")
        await asyncio.sleep(.10)
        await message.edit(content="(╯°□°)╯      ┻━┻")

    @commands.command()
    async def tableflop(self, ctx):
        message = await ctx.send("(\\\\°□°)\\\\  ┬─┬')")
        await asyncio.sleep(.10)
        await message.edit(content="(-°□°)-  ┬─┬")
        await asyncio.sleep(.20)
        await message.edit(content="┬─┬ ノ( ゜-゜ノ)")

    # Dice Command
    # >dice
    @commands.command()
    async def roll(self, ctx):
        choices = ["1", "2", "3", "4", "5", "6"]
        chosen = random.choice(choices)
        await ctx.send(f"The Dice has Choosen {chosen}")

    # Love Command
    # >love <word>
    @commands.command()
    async def love(self, ctx, word: str):
        chosen = random.randint(0, 10)
        if chosen == "0":
            hearts = ":broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: "
        elif chosen == "1":
            hearts = ":heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: "
        elif chosen == "2":
            hearts = ":heart: :heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart::broken_heart: :broken_heart: :broken_heart: :broken_heart:"
        elif chosen == "3":
            hearts = ":heart: :heart: :heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart:"
        elif chosen == "4":
            hearts = ":heart: :heart: :heart: :heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart:"
        elif chosen == "5":
            hearts = ":heart: :heart: :heart: :heart: :heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart:"
        elif chosen == "6":
            hearts = ":heart: :heart: :heart: :heart: :heart: :heart: :broken_heart: :broken_heart: :broken_heart: :broken_heart:"
        elif chosen =="7":
            hearts = ":heart: :heart: :heart: :heart: :heart: :heart: :heart: :broken_heart: :broken_heart: :broken_heart:"
        elif chosen == "8":
            hearts = ":heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :broken_heart: :broken_heart:"
        elif chosen == "9":
            hearts = ":heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :broken_heart:"
        else:
            hearts = ":heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart:"
        await ctx.send(f"You love {word} {chosen}/10\n{hearts}")

    # Dad Joke Command
    # >dadjoke
    @commands.command()
    async def dadjoke(self, ctx):
        jokes = ["What time did the man go to the dentist? Tooth hurt-y", "I'm reading a book about anti-gravity. It's impossible to put down!", "Want to hear a joke about a piece of paper? Never mind... it's tearable.", "I just watched a documentary about beavers. It was the best dam show I ever saw!", "If you see a robbery at an Apple Store does that make you an iWitness?", "Spring is here! I got so excited I wet my plants!", "A ham sandwich walks into a bar and orders a beer. The bartender says, \"Sorry we don’t serve food here.\"", "What’s Forrest Gump’s password? 1forrest1", "I bought some shoes from a drug dealer. I don't know what he laced them with, but I was tripping all day!", "Why do chicken coops only have two doors? Because if they had four, they would be chicken sedans!", "What do you call a factory that sells passable products? A satisfactory.", "A termite walks into a bar and asks, \"Is the bar tender here?\"", "When a dad drives past a graveyard: Did you know that's a popular cemetery? Yep, people are just dying to get in there!", "Two peanuts were walking down the street. One was a salted.", "Why did the invisible man turn down the job offer? He couldn't see himself doing it.", "I used to have a job at a calendar factory but I got the sack because I took a couple of days off.", "How do you make holy water? You boil the hell out of it.", "A three-legged dog walks into a bar and says to the bartender, \"I’m looking for the man who shot my paw.\"", "When you ask a dad if he's alright: \"No, I’m half left.\"", "I had a dream that I was a muffler last night. I woke up exhausted!", "How do you tell the difference between a frog and a horny toad? A frog says, \"Ribbit, ribbit\" and a horny toad says, \"Rub it, rub it.\"", "Did you hear the news? FedEx and UPS are merging. They’re going to go by the name Fed-Up from now on.", "5/4 of people admit that they’re bad with fractions.", "MOM: \"How do I look?\" DAD: \"With your eyes.\"", "What is Beethoven’s favorite fruit? A ba-na-na-na.", "What did the horse say after it tripped? \"Help! I’ve fallen and I can’t giddyup!\”", "Did you hear about the circus fire? It was in tents!", "Don't trust atoms. They make up everything!", "What do you get when you cross an elephant with a rhino? Elephino.", "How many tickles does it take to make an octopus laugh? Ten-tickles.", "What's the best part about living in Switzerland? I don't know, but the flag is a big plus.", "What do prisoners use to call each other? Cell phones.", "Why couldn't the bike standup by itself? It was two tired.", "What do you call a dog that can do magic? A Labracadabrador.", "Why didn't the vampire attack Taylor Swift? She had bad blood.", "NURSE: \"Blood type?\" DAD: \"Red.\"", "SERVER: \"Sorry about your wait.\" DAD: \"Are you saying I’m fat?\”", "What do you call a fish with two knees? A “two-knee” fish.", "I was interrogated over the theft of a cheese toastie. Man, they really grilled me.", "What do you get when you cross a snowman with a vampire? Frostbite.", "Can February March? No, but April May!", "When you ask a dad if they got a haircut: \"No, I got them all cut!\"", "What does a zombie vegetarian eat? “GRRRAAAAAIIIINNNNS!”", "What does an angry pepper do? It gets jalapeño your face.", "Why wasn't the woman happy with the velcro she bought? It was a total ripoff.", "What did the buffalo say to his son when he dropped him off at school? Bison.", "What do you call someone with no body and no nose? Nobody knows.", "Where did the college-aged vampire like to shop? Forever 21.", "You heard of that new band 1023MB? They're good but they haven't got a gig yet.", "Why did the crab never share? Because he's shellfish."]
        await ctx.send(f"{random.choice(jokes)}")

    # Cuddle Command
    # >cuddle <member>
    @commands.command()
    async def cuddle(self, ctx, member: discord.Member = None):
        if member == ctx.author or member == None:
            await ctx.send(f"APPARENTLY {ctx.author.mention} Some how cuddle with themselves ...weird")
        else:
            await ctx.send(f"{ctx.author.mention} Cuddled with {member.mention}. Very Cute UwU")
    
    
    @commands.command()
    async def furry(self, ctx, user: discord.Member = None):
        chosen = random.randint(0, 10)
        if user == ctx.author or user == None:
            await ctx.send(f"You are {chosen}/10 Furry!")
        else:
            await ctx.send(f"{user.mention} is {chosen}/10 Furry")

    @commands.command()
    async def cry(self, ctx):
        await ctx.send(f"{ctx.author.mention} Cried. ;-;")

    @commands.command()
    async def lick(self, ctx, user: discord.Member = None):
        if user == ctx.author or user == None:
            lickEmbed = discord.Embed(title = "Licked a User", description = f"{ctx.author.mention} licked themselves that is some fucked up wizard shit mannnn")
        else:
            lickEmbed = discord.Embed(title="Licked a User", description = f"{ctx.author.mention} licked {user.mention} 👅")
        lickEmbed.set_image(url="https://media.discordapp.net/attachments/714681336652103750/744380390151815279/oyn30Ku1Nf0.gif")
        lickEmbed.set_footer(text="I stole your toes")
        await ctx.send(embed=lickEmbed)

    @commands.command()
    async def lick(self, ctx, user: discord.Member = None):
        if user == ctx.author or user == None:
            lickEmbed = discord.Embed(title = "Licked a User", description = f"{ctx.author.mention} licked themselves that is some fucked up wizard shit mannnn")
        else:
            lickEmbed = discord.Embed(title="Licked a User", description = f"{ctx.author.mention} licked {user.mention} 👅")
        lickEmbed.set_image(url="https://media.discordapp.net/attachments/714681336652103750/744380390151815279/oyn30Ku1Nf0.gif")
        lickEmbed.set_footer(text="I stole your toes")
        await ctx.send(embed=lickEmbed) 

        """TODO: FIX"""

    """ @commands.command()
    async def owo(self, ctx):
        response = requests.get('https://rra.ram.moe/i/r?type=owo')
        jsonRes = response.json
        if response:
            owoEmbed = discord.Embed(title="OWO WHAT'S THIS")
            owoEmbed.set_image(url=f"https://rra.ram.moe{jsonRes.path}")
            await ctx.send(embed=owoEmbed)
        else:
            await ctx.send("An Error has Occured, contact the bot devs") """

    @commands.command()
    async def stare(self, ctx, user: discord.Member = None):
        if user == ctx.author or user == None:
            stareEmbed = discord.Embed(title = "Stare at a User", description = f"{ctx.author.mention} stares at themselves in the mirror")
        else:
            stareEmbed = discord.Embed(title="Stare at a User", description = f"{ctx.author.mention} stares at {user.mention} 👀 that really creepy and fucked up")
        stareEmbed.set_image(url="https://media.discordapp.net/attachments/731523556801773769/744695058120441866/tenor.gif?width=302&height=401")
        stareEmbed.set_footer(text="I stole your toes")
        await ctx.send(embed=stareEmbed)


def setup(bot): bot.add_cog(Fun(bot))
