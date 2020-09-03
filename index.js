const Discord = require('discord.js');
const bot = new Discord.Client();
const token = 'put_token_here';
const on_sale_url = 'https://store.steampowered.com/search/?category1=998&os=win&specials=1';
var fs = require("fs");
var text = fs.readFileSync("./games.txt");
var textByLine = text.toString().split("\n")

bot.on('ready',() => {
	console.log("The bot is online");
})
bot.on('message', msg=> {
	if(msg.content === "/game"){
		var x = Math.floor((Math.random() * textByLine.length) + 1);
		msg.reply(""+textByLine[x]);
	}
})
bot.login(token);
