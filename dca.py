#!/usr/bin/env python3
import discord
import sys
if sys.argv[0] == "python3" or sys.argv[0] == "python":
	del sys.argv[0]

del sys.argv[0]
if len(sys.argv) < 1:
	print("Insufficient Arguments")
	quit()
arg_count = 1

send_list = []


while arg_count < len(sys.argv):
	if sys.argv[arg_count][0] == "c":
		if arg_count + 1 < len(sys.argv):
			send_list.append(["c", sys.argv[arg_count][1:], sys.argv[arg_count + 1]])
	if sys.argv[arg_count][0] == "d":
		if arg_count + 1 < len(sys.argv):
			send_list.append(["d", sys.argv[arg_count][1:], sys.argv[arg_count + 1]])
	arg_count += 1

client = discord.Client()

@client.event
async def on_ready():
	try:
		for message in send_list:
			if message[0] == "c":
				channel = client.get_channel(int(message[1]))
				await channel.send(message[2])
			if message[0] == "d":
				user = client.get_user(int(message[1]))
				await user.send(message[2])
	except Exception as exc:
		print("Error in execution: " + str(exc))
	await client.close()

client.run(sys.argv[0])
