# import required dependencies
import discord
from discord.ext import commands

# import Bot Token
from apikeys import

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="lofi hip hop"))
    print("The bot is now ready for use")
    print("-----------------------------")


@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am a student bot use \"/help\" for commands")


@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command!")


@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Student bot left the voice channel")
    else:
        await ctx.send("I am not in a voice channel!")


@client.event
async def on_message(message):
    user_mesg = message.content.lower()

    if user_mesg == "office hours" or user_mesg == "office hour":
        await message.channel.send("Office hours is Wednesday (11am - 1pm), either in zoom or in PKI 285B")
    if user_mesg == "accommodations" or user_mesg == "accessibility":
        await message.channel.send("If you have any accommodations I need to be aware of, please reach out to the "
                                   "accessibility office before the end of the first week, to get official "
                                   "documentation.")

    await client.process_commands(message)


@client.command()
async def syllabus(ctx):
    embed = discord.Embed(title="Syllabus", url="https://unomaha.instructure.com/courses/65276/files/7661598?wrap=1", description="This is the course Syllabus!", color=0x0000cc)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.set_thumbnail(url="https://www.unomaha.edu/_files/images/uno-icon-50.png")
    await ctx.send(embed=embed)

@client.command()
async def accommodations(ctx):
    await ctx.send("If you have any accommodations I need to be aware of, please reach out to the accessibility "
                   "office before the end of the first week, to get official documentation.")
    await ctx.send("To get an accommodation for a missed lab, test, or project, you must send an email to the "
                   "accessibility office. They are the responsible for validating any documentation you might have ("
                   "doctor’s note etc.) and reaching out to me to formally ask for an accommodation on your beh")

@client.command()
async def plagiarism(ctx):
    await ctx.send("If you have any accommodations I need to be aware of, please reach out to the accessibility "
                   "office before the end of the first week, to get official documentation")
    await ctx.send("To get an accommodation for a missed lab, test, or project, you must send an email to the "
                   "accessibility office. They are the responsible for validating any documentation you might have ("
                   "doctor’s note etc.) and reaching out to me to formally ask for an accommodation on your behalf")
@client.command()
async def topics(ctx):
    await ctx.send("Below is a list of topics that will be covered in the class.")
    await ctx.send("1. Programming Structures\n2. Data Structures\n3. Modules\n"
                   "4. Files\n5. Exceptions\n6. Algorithm Analysis\n7. Recursion\n"
                   "8. Searching and Sorting\n9. Object Oriented Programming\n"
                   "10. Graphical User Interfaces\n11. Testing\n12. Documentation")

@client.command()
async def objectives(ctx):
    await ctx.send("By the end of this course, students will:")
    await ctx.send("1. Use elementary control structures to write program\n"
                   "2. Use appropriate built-in data structures to store and manipulate\n"
                   "3. Use built-in libraries to write programs and develop user defined modules.\n"
                   "4. Design programs that perform file operations.\n"
                   "5. Handle runtime errors gracefully through exception handling.\n"
                   "6. Analyze algorithms in terms of their time and space complexity."
                   "7. Design recursive algorithms to solve problems of a recursive nature.\n"
                   "8. Analyze different searching and sorting algorithms.\n"
                   "9. Use object-oriented programming techniques to design programs.\n"
                   "10. Develop Graphical User Interfaces for programs.\n"
                   "11. Develop unit test cases to check program behavior.\n"
                   "12. Manage software changes using version control tools.")

@client.command()
async def policies(ctx):
    await ctx.send("-Lectures and Class Material")
    await ctx.send("\tThe lecture videos explain the notes provided.\n"
                   "\tSome topics have review questions provided for practice.\n"
                   "\tThe discord server will be used as a discussion platform where announcements, resources, "
                   "and answers to any questions asked regarding the class material will be posted. Anyone can "
                   "respond to a question posted to the server.")
    await ctx.send("\n\n-Labs and Project")
    await ctx.send("You are allowed to work individually or in groups of 2. If you choose to work in a group, "
                   "only 1 person needs to make a submission (make sure you include your groupmate’s name in the "
                   "comment section.")
    await ctx.send("Late work will receive a grade of 0")
    await ctx.send("Please check your submissions to ensure you have submitted the right files with the correct names "
                   "according to the lab/project instructions")
    await ctx.send("You can use office hours, class sessions, and lab sessions to get feedback on your lab/project "
                   "before making a final submission.")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission to run this command")
    if isinstance(error, commands.CommandError):
        await ctx.send("Please enter command correctly")



client.run(bottoken)