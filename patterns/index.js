const patternDict = [
		{
		pattern : '\\b(?<greeting>Hi|Hello|Hey|Bonjour|Salut)\\b',
		intent : 'Hello'
		},	
		{
		pattern :'\\b(?<song>[A-Za-z])\\b' ,
		intent: 'Song',
		entities : {
					name:'songs'
				   }
		},
		{
		pattern :'\\b(bye|see you)\\b',
		intent : 'Exit'
		}
	];
module.exports = patternDict ;