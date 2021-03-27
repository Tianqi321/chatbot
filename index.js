var Discord=require("discord.js")
var client = new Discord.Client();
const matcher = require ('./matcher') ;
let jsexecpy = require("jsexecpy");
let callback = function({data,pythonpath},otherargs = 11){
    dosomething(data,pythonpath,otherargs)
}

client.on('reday',function(){
    console.log("Successfully connected")
})


client.on('message',function(msg){
    if(msg.author == client.user){return;}
    else{ 
        matcher (msg.content , cb => {
            switch(cb.intent){
                case 'Hello':
                    msg.channel.send('Deadpool:Hi!Nice to meet you,i am Deadpool,your Discord Music Bot!');
                    msg.channel.send('Deadpool:May i ask what is your favorite music?(Due to some limits we dont have many songs in database!)');                                           
                    break
                case 'Exit':
                    msg.channel.send('Deadpool:Goodbye, hope to meet u next time,i am Deadpool,your Discord Music Bot!');
                    break
                case 'Song':
                    msg.channel.send('Deadpool:Great, i love this song too');
                    break
                default:
                    jsexecpy.runpath("./rec.py",callback)
                    msg.channel.send('Deadpool:Sorry,i dont really understand you ,please advice me at tianqi.huang@edu.devinci.fr');
                    break
            }
            }) ;
        }
});
        
client.login('ODI1MTQwMTI2NzE0ODIyNjY3.YF5loA.Vhgt1uvD1Ger7mKz78UY8vzzfdw')