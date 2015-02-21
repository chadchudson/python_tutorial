class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
               
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

class Crazy(object):
    
    def __init__(self, comment):
        self.comment = comment

        
    def tell_me_about_it(self):
        for line in self.comment:
            print line


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song (["They rally around the family",
                         "With pockets full of shells"])

testing_a_new_lyric = Song (["Whatever, this is driving me nuts",
                             "I'm not that big of a fan of music anyway."])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

testing_a_new_lyric.sing_me_a_song()

this_is_insane = Crazy (["This OOP stuff is hurting my head",
                         "But, I really want to figure it out."])

keep_trying = Crazy (["So, I am going to continue trying",
                      "remember, functions became clear too!"])

this_is_insane.tell_me_about_it()
keep_trying.tell_me_about_it()

