import random
import os

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Card():
   def __init__(self,suits,ranks):
       self.suits = suits
       self.ranks = ranks

   def __str__(self):
         return('-->' + f'{self.ranks} of {self.suits}')
    
class Deck(Card):
    
    def __init__(self,listdeck=[]):
        self.listdeck = listdeck
        for suit in suits:
            for rank in ranks:
                   newcard = Card(suit,rank)
                   listdeck.append(newcard)
    
    def shuffle(self):
        random.shuffle(self.listdeck)
            
        
    def __str__(self):
        count = 0
        for i in self.listdeck:
            count = count + 1
            print(i)
        return(f'Total cards : {count}')    
    
    def hit(self):
        random.shuffle(self.listdeck)
        return(self.listdeck.pop())
    
    


class Player():
    def __init__(self,name,total=100,bet=0,cards=[],score=0):
        self.name = name
        self.total = total
        self.bet = bet
        self.cards = cards
        self.score = score
        
    def start(self):
        card1 = Deck().hit()
        card2 = Deck().hit()
        self.cards = [card1,card2]
        return(self.cards)
    
    def sumer(self):
        self.score = 0
        for i in self.cards:
            self.score = self.score + values[i.ranks]
        return(self.score)
    
    def hit(self):
            card = Deck().hit()
            print(f'Player {self.name} hits another card and the card is : {card}')
            self.cards.append(card)
            return(self.cards)
    
    def win_bet(self):
        self.total = self.total + self.bet 
        return(self.total)
    
    def lose_bet(self):
        self.total = self.total - self.bet
        return(self.total)            
            

class Dealer():
    
    def __init__(self,cards=[],score=0):
          self.score = score
          self.cards = cards
      
    def start(self):
        card1 = Deck().hit()
        card2 = Deck().hit()
        self.cards = [card1,card2]
        return(self.cards)
        
    def sumer(self,start):
        self.score = 0
        if(start == 1):
            for i in self.cards:
                self.score = self.score + values[i.ranks]   
            return(self.score - values[self.cards[0].ranks])
        else:
             for i in self.cards:
                self.score = self.score + values[i.ranks]
             return(self.score) 
           
    def hit(self):
        card = Deck().hit()
        print(f'Dealer hits another card and the card is : {card}')
        self.cards.append(card)
        return(self.cards)
        
        
def take_bet(name):
    while(True):
        try:
            bet = int(input(f'{name.capitalize()} please give me your starting bet\n'))
        except:
            bet = print('Try again!')
        else:
            return(bet)
            break                       
              
def take_chips(name):
    while(True):
        try:
            chips = int(input(f'{name.capitalize()} how many chips do you have?\n'))
        except:
            chips = print('Try again!')
        else:
            return(chips)
            break      
        
def print_some(cards):
    for i in cards:
        if i == cards[0]:
            continue
        else:
            print(i)
            
def print_all(cards):
    for i in cards:
        print(i)

def decision(name):
     choice =input(f'{name.capitalize()} Hit or Stand?\n')
     if((choice == 'hit') or (choice == 'HIT') or (choice == 'Hit')):
                return(0)
     else:
         return(1)     
              
def start():
    while(True):
        start = 1
        deck = Deck()
        name = input('Please give me your name\n')
        chips = take_chips(name)
        bet = take_bet(name)
        while(bet > chips):
            print('Sorry you can not bet more than you have') 
            bet = take_bet()
            
        player = Player(name,chips,bet)  
        player_cards = player.start()  
        
        deck.shuffle()
        
        dealer = Dealer()
        dealer_cards = dealer.start()
        os.system('clear')
        
        print(f'Lets begin with Dealer.The one of his two cards is:')
        print_some(dealer_cards)
        deal_sum = dealer.sumer(start)
        print(f'With the value of the card: {deal_sum}')
        print('\n')
        
        print(f'{name.capitalize()} your first two cards are:')
        print_all(player_cards)
        play_sum = player.sumer()
        print(f'With total value of: {play_sum}')
        
        option = decision(name)
        while(option==0):
            player_cards=player.hit()
            print_all(player_cards)
            play_sum = player.sumer()
            print(f"Total value of your cards is {play_sum}")
            if(play_sum > 21):
                print(f'{name} you busted.The sum : {play_sum} is over 21.Dealer wins')
                chips = player.lose_bet()
                print(f'Now your chips are: {chips}')
                return(0)
            option = decision(name)
        
        print('\n')
        start = 0    
        print("It's dealers turn.")         
        while(deal_sum < 17):
            dealer_cards = dealer.hit() 
            print_all(dealer_cards)
            deal_sum = dealer.sumer(start)
            print(f"Total dealer's value is {deal_sum}")
            print('\n')
            if(deal_sum > 21):
                print(f'Dealer busted.{name.capitalize()} wins')
                chips = player.win_bet()
                print('\n')
                print(f'Now your chips are: {chips}')
                return(0)
            
        if(deal_sum > play_sum):
            print('Dealer Wins')   
            chips = player.lose_bet()
            print('\n')
            print(f'Now {name.capitalize()} your chips are: {chips}')            
            return(0)
        else:
            print(f'{name.capitalize()}) Wins')
            chips = player.win_bet()
            print(f'Now {name.capitalize()} your chips are: {chips}') 
            return(0)
            
        
start()        
while(True):       
    choice=input('Do you want to play again? yes or no\n')
    if(choice == 'yes'):
        os.system('clear')
        start()
    else:
        break    
