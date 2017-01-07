##This software is distributed under a BSD license.

##Copyright (c) 2008--2017, CodeMartyLikeYou
##All rights reserved.
##
##Redistribution and use in source and binary forms, with or without
##modification, are permitted provided that the following conditions are met:
##    * Redistributions of source code must retain the above copyright
##      notice, this list of conditions and the following disclaimer.
##    * Redistributions in binary form must reproduce the above copyright
##      notice, this list of conditions and the following disclaimer in the
##      documentation and/or other materials provided with the distribution.
##    * Neither the name of the <organization> nor the
##      names of its contributors may be used to endorse or promote products
##      derived from this software without specific prior written permission.
##
##THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
##ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
##WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
##DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
##DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
##(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
##LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
##ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
##(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
##SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import networkx as nx
import copy, os
import Tkinter as tk
from functools import partial
#from PIL.ImageTk import PhotoImage
#from PIL import Image
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

####################################################################################
##Data
####################################################################################
execfile(resource_path(os.path.join('data','EvoDict.txt'))) #loads EvoDict. How to use: EvoDict[monster][meat] = result

#wX or wXnoboss (X a number from 1 to 10) = set of all meats in world X, containing or not containing boss meats:
#1=First            2=Ashura     3=Giant's and inside Ki
#4=Apollo           5=Guardians  6=Venus's City and sewers
#7=Volcano          8=Race       9=Edo
#10=Nasty 1-5 and Valhalla
#11=Nasty 6-8 and Final
#12=Celestial
#good
w1bosses=list(['Babywyrm','Rhino'])
w1noboss=set(['Fly', 'Skelton', 'Jaguar', 'Toad', 'Spider', 'Fungus', 'Lizard', 'Goblin'])

#good
w2bosses=list(['Woodman'])
w2noboss=set(['Eagle', 'Babywyrm', 'Slime', 'Zombie', 'Wererat', 'Flower', 'Barracud', 'Snake', 'Beetle', 'Redbone', 'Pebble', 'Octopus'])

#good
w3bosses=list(['Phagocyt'])
w3noboss=set(['Woodman', 'Oni', 'Grippe', 'Cobble', 'Worm', 'Amoeba', 'Crab', 'Fiend', 'Rhino', 'Plasma', 'Silver'])

#good
w4bosses=[]
w4noboss=set(['Wyrmkid', 'Tortoise', 'Moth', 'Jelly', 'Phagocyt', 'Virus', 'Cameleon', 'Hofud', 'Kelpie', 'Mapleman', 'Raven', 'Medusa', 'Griffon', 'Bigeye', 'Pspider', 'Ghoul', 'Sabrecat'])

#good
w5noboss=set(['Hornet', 'Liveork', 'Mushroom', 'Obake', 'Pworm', 'Werewolf'])
w5bosses=list(['Ogre', 'Mantcore'])

#good - phantom, mephisto, hermit not considered bosses
w6bosses=[]
w6noboss=set(['Turtle', 'Sprite', 'Mushroom', 'Werewolf', 'Thunder', 'Harpy', 'Obake', 'Liveork', 'Hornet', 'Babyd', 'Ptoad', 'Chafer', 'Pworm', 'Clayman','Hermit','Mephisto','Phantom'])

#good
w7bosses=[]
w7noboss=set(['Ammonite', 'Corpuscl', 'Triceras', 'Ogre', 'Serpent', 'Tororo', 'Mantcore', 'Antlion', 'Champgno', 'Pflower', 'Piranha', 'Komodo', 'Warrior', 'Swallow'])

#good
w8bosses=['Adamant','Tortoise','Lamia','Watcher']
w8noboss=set(['Ammonite', 'Corpuscl', 'Triceras', 'Ogre', 'Serpent', 'Tororo', 'Mantcore', 'Antlion', 'Champgno', 'Pflower', 'Piranha', 'Komodo', 'Warrior', 'Swallow'])

#good
w9bosses=[]
w9noboss=set(['Boulder', 'Phantom', 'Tarantla', 'Gaebolg', 'Gazer', 'Mosquito', 'Anaconda', 'Evilpine', 'Wyvern', 'Fairy', 'Hermit', 'Stoneman', 'Pathogen', 'Mephisto'])

#good
w10bosses=['Odincrow','Sleipnir']
w10noboss=set(['Catwoman', 'Answerer', 'Snowcat', 'Lamia', 'Nitemare', 'Demon', 'Shark', 'Lavaworm', 'Ghast', 'Dinosaur', 'Firemoth', 'Youngd', 'Adamant', 'Wraith'])

#good
w11bosses=[]
w11noboss=set(['Fflower', 'Tengu', 'Nymph', 'Watcher', 'Icecrab', 'Chimera', 'Naga', 'Cocatris', 'Dragon', 'Hugetoad'])

#good
w12bosses=['Tianlung','Fenrir']
w12noboss=set(['Giant', 'Spector', 'Giantoad', 'Rakshasa', 'Shiitake', 'Hydra', 'Gunfish', 'Salamand', 'Boneking', 'Sleipnir', 'Garuda', 'Demoload', 'Sylph', 'Wight', 'Cicada', 'Plague', 'Ironman', 'Wyrm', 'Moaner', 'Fspider', 'Gloom', 'Scylla', 'Sphinx', 'Blackcat', 'Trex', 'Pudding', 'Squid', 'Rock', 'Evileye', 'Cfisher', 'Sandworm', 'Kingcrab', 'Cancer', 'Roc', 'Madcedar', 'Greatd', 'Sunplant', 'Dturtle'])

noboss_list=[w1noboss,w2noboss,w3noboss,w4noboss,w5noboss,w6noboss,w7noboss,w8noboss,w9noboss,w10noboss,w11noboss,w12noboss]
boss_list=[w1bosses,w2bosses,w3bosses,w4bosses,w5bosses,w6bosses,w7bosses,w8bosses,w9bosses,w10bosses,w11bosses,w12bosses]


#all_meats contains every meat you can find in the game
all_meats=set(['Nitemare', 'Babywyrm', 'Nymph', 'Moaner', 'Piranha', 'Hydra', 'Flower', 'Fiend', 'Evilpine', 'Raven', 'Garuda', 'Pflower', 'Sylph', 'Wight', 'Wererat', 'Snake', 'Wyvern', 'Adamant', 'Sabrecat', 'Giantoad', 'Tortoise', 'Komodo', 'Catwoman', 'Blackcat', 'Antlion', 'Demon', 'Cfisher', 'Ghoul', 'Shark', 'Kingcrab', 'Cancer', 'Squid', 'Cobble', 'Watcher', 'Icecrab', 'Naga', 'Sphinx', 'Medusa', 'Pspider', 'Wraith', 'Thunder', 'Obake', 'Rhino', 'Barracud', 'Dturtle', 'Boneking', 'Plasma', 'Hugetoad', 'Pathogen', 'Warrior', 'Woodman', 'Cocatris', 'Kelpie', 'Harpy', 'Virus', 'Plague', 'Grippe', 'Wyrm', 'Fspider', 'Scylla', 'Worm', 'Gaebolg', 'Trex', 'Pudding', 'Hofud', 'Mapleman', 'Redbone', 'Swallow', 'Bigeye', 'Octopus', 'Hornet', 'Turtle', 'Ogre', 'Pworm', 'Roc', 'Spider', 'Gazer', 'Cicada', 'Beetle', 'Sunplant', 'Pebble', 'Odincrow', 'Giant', 'Rakshasa', 'Rock', 'Madcedar', 'Snowcat', 'Evileye', 'Hermit', 'Boulder', 'Zombie', 'Wyrmkid', 'Triceras', 'Tarantla', 'Toad', 'Fungus', 'Liveork', 'Lamia', 'Stoneman', 'Fly', 'Ammonite', 'Fenrir', 'Mephisto', 'Werewolf', 'Mantcore', 'Amoeba', 'Cameleon', 'Babyd', 'Fairy', 'Lavaworm', 'Tororo', 'Serpent', 'Tengu', 'Tianlung', 'Gloom', 'Champgno', 'Chimera', 'Greatd', 'Ptoad', 'Youngd', 'Clayman', 'Phantom', 'Corpuscl', 'Answerer', 'Shiitake', 'Phagocyt', 'Gunfish', 'Griffon', 'Salamand', 'Crab', 'Fflower', 'Eagle', 'Sleipnir', 'Sprite', 'Mushroom', 'Demoload', 'Firemoth', 'Ironman', 'Goblin', 'Silver', 'Spector', 'Skelton', 'Jaguar', 'Jelly', 'Dinosaur', 'Lizard', 'Mosquito', 'Dragon', 'Ghast', 'Oni', 'Sandworm', 'Moth', 'Slime', 'Anaconda', 'Chafer'])
#name_to_family_and_level translates from creature name to family name + level. Includes all monsters in the game, incluidng pc-only and npc-only
name_to_family_and_level={'Nitemare': ('Silver', 2), 'Flower': ('Flower', 0), 'Nymph': ('Sprite', 2), 'Moaner': ('Hofud', 3), 'Piranha': ('Barracud', 1), 'Starterslime': ('Slime', -1), 'Hydra': ('Snake', 3), 'Babywyrm': ('Babywyrm', 0), 'Fiend': ('Fiend', 0), 'Evilpine': ('Mapleman', 2), 'Raven': ('Raven', 0), 'Titania': ('Sprite', 4), 'Jorgandr': ('Snake', 4), 'Garuda': ('Raven', 3), 'Pflower': ('Flower', 1), 'Sylph': ('Sprite', 3), 'Wight': ('Zombie', 3), 'Wererat': ('Wererat', 0), 'Snake': ('Snake', 0), 'Basilisk': ('Lizard', 4), 'Wyvern': ('Babywyrm', 2), 'Adamant': ('Tortoise', 2), 'Sabrecat': ('Jaguar', 1), 'Giantoad': ('Toad', 3), 'Tortoise': ('Tortoise', 0), 'Komodo': ('Lizard', 2), 'Kraken': ('Octopus', 4), 'Catwoman': ('Wererat', 2), 'Mantis': ('Fly', 4), 'Blackcat': ('Jaguar', 3), 'Kirin': ('Griffon', 4), 'Susanoo': ('Goblin', 4), 'Antlion': ('Beetle', 2), 'Demon': ('Fiend', 2), 'Cfisher': ('Beetle', 3), 'Kingtoad': ('Toad', 4), 'Ghoul': ('Zombie', 1), 'Shark': ('Barracud', 2), 'Kingcrab': ('Crab', 3), 'Cancer': ('Plasma', 3), 'Seiryu': ('Babyd', 4), 'Squid': ('Octopus', 3), 'Cobble': ('Pebble', 1), 'Watcher': ('Bigeye', 2), 'Icecrab': ('Crab', 2), 'Naga': ('Medusa', 2), 'Sphinx': ('Griffon', 3), 'Medusa': ('Medusa', 0), 'Slimegod': ('Slime', 4), 'Pspider': ('Spider', 1), 'Wraith': ('Obake', 2), 'Ghost': ('Obake', 4), 'Arachne': ('Spider', 4), 'Thunder': ('Eagle', 1), 'Obake': ('Obake', 0), 'Rhino': ('Rhino', 0), 'Barracud': ('Barracud', 0), 'Dturtle': ('Tortoise', 3), 'Boneking': ('Skelton', 3), 'Plasma': ('Plasma', 0), 'Hugetoad': ('Toad', 2), 'Pathogen': ('Grippe', 2), 'Warrior': ('Skelton', 2), 'Woodman': ('Woodman', 0), 'Cocatris': ('Eagle', 2), 'Kelpie': ('Silver', 1), 'Harpy': ('Raven', 1), 'Byakko': ('Jaguar', 4), 'Virus': ('Grippe', 1), 'Plague': ('Grippe', 3), 'Grippe': ('Grippe', 0), 'Wyrm': ('Babywyrm', 3), 'Suzaku': ('Eagle', 4), 'Fspider': ('Spider', 3), 'Scylla': ('Medusa', 3), 'Behemoth': ('Rhino', 4), 'Worm': ('Worm', 0), 'Gaebolg': ('Hofud', 1), 'Trex': ('Rhino', 3), 'Pudding': ('Slime', 3), 'Hofud': ('Hofud', 0), 'Mapleman': ('Mapleman', 0), 'Redbone': ('Skelton', 1), 'Swallow': ('Moth', 1), 'Bigeye': ('Bigeye', 0), 'Octopus': ('Octopus', 0), 'Hornet': ('Fly', 1), 'Turtle': ('Tortoise', 1), 'Ogre': ('Goblin', 2), 'Pworm': ('Worm', 1), 'Roc': ('Eagle', 3), 'Spider': ('Spider', 0), 'Gazer': ('Bigeye', 1), 'Cicada': ('Fly', 3), 'Beetle': ('Beetle', 0), 'Sunplant': ('Flower', 3), 'Pebble': ('Pebble', 0), 'Odincrow': ('Fenrir', 1), 'Starterbabyd': ('Babyd', -1), 'Giant': ('Goblin', 3), 'Nike': ('Raven', 4), 'Rakshasa': ('Wererat', 3), 'Rock': ('Pebble', 3), 'Imp': ('Fiend', -1), 'Madcedar': ('Mapleman', 3), 'Snowcat': ('Jaguar', 2), 'Madame': ('Moth', 4), 'Evileye': ('Bigeye', 3), 'Hermit': ('Crab', 1), 'Boulder': ('Pebble', 2), 'Zombie': ('Zombie', 0), 'Wyrmkid': ('Babywyrm', 1), 'Triceras': ('Rhino', 1), 'Tarantla': ('Spider', 2), 'Toad': ('Toad', 0), 'Lilith': ('Medusa', 4), 'Fungus': ('Fungus', 0), 'Liveork': ('Mapleman', 1), 'Lamia': ('Medusa', 1), 'Genbu': ('Tortoise', 4), 'Stoneman': ('Woodman', 2), 'Fly': ('Fly', 0), 'Ammonite': ('Octopus', 2), 'Fenrir': ('Fenrir', 0), 'Mephisto': ('Fiend', 1), 'Werewolf': ('Wererat', 1), 'Revenant': ('Zombie', 4), 'Mantcore': ('Griffon', 1), 'Amoeba': ('Octopus', 1), 'Cameleon': ('Lizard', 1), 'Babyd': ('Babyd', 0), 'Fairy': ('Sprite', 1), 'Lavaworm': ('Worm', 2), 'Tororo': ('Slime', 2), 'Serpent': ('Snake', 1), 'Fenglung': ('Babywyrm', 4), 'Tengu': ('Raven', 2), 'Tianlung': ('Tianlung', 0), 'Gloom': ('Moth', 3), 'Champgno': ('Fungus', 2), 'Chimera': ('Griffon', 2), 'Greatd': ('Babyd', 3), 'Ptoad': ('Toad', 1), 'Youngd': ('Babyd', 1), 'Clayman': ('Woodman', 1), 'Phantom': ('Obake', 1), 'Corpuscl': ('Plasma', 2), 'Dagon': ('Crab', 4), 'Answerer': ('Hofud', 2), 'Shiitake': ('Fungus', 3), 'Beholder': ('Bigeye', 4), 'Phagocyt': ('Plasma', 1), 'Gunfish': ('Barracud', 3), 'Griffon': ('Griffon', 0), 'Salamand': ('Lizard', 3), 'Crab': ('Crab', 0), 'Mazin': ('Woodman', 4), 'Fflower': ('Flower', 2), 'Scarab': ('Beetle', 4), 'Eagle': ('Eagle', 0), 'Sleipnir': ('Silver', 3), 'Sprite': ('Sprite', 0), 'Mushroom': ('Fungus', 1), 'Gigaworm': ('Worm', 4), 'Demoload': ('Fiend', 3), 'Kusanagi': ('Hofud', 4), 'Unicorn': ('Silver', 4), 'Firemoth': ('Moth', 2), 'Ironman': ('Woodman', 3), 'Goblin': ('Goblin', 0), 'Silver': ('Silver', 0), 'Spector': ('Obake', 3), 'Skelton': ('Skelton', 0), 'Jaguar': ('Jaguar', 0), 'Jelly': ('Slime', 1), 'Darkrose': ('Flower', 4), 'Dinosaur': ('Rhino', 2), 'Lizard': ('Lizard', 0), 'Mosquito': ('Fly', 2), 'Dragon': ('Babyd', 2), 'Lich': ('Skelton', 4), 'Ghast': ('Zombie', 2), 'Oni': ('Goblin', 1), 'Sandworm': ('Worm', 3), 'Moth': ('Moth', 0), 'Anubis': ('Wererat', 4), 'Treant': ('Mapleman', 4), 'Slime': ('Slime', 0), 'Toadstol': ('Fungus', 4), 'Leviathan': ('Barracud', 4), 'Athtalot': ('Fiend', 4), 'Anaconda': ('Snake', 2), 'Earth': ('Pebble', 4), 'Chafer': ('Beetle', 1)}

#family_to_members translates from family name (e.g., 'Sprite') to a list containing tuples of the form (monster, level). The list is sorted by level.
family_to_members={}
for _monster,_val in name_to_family_and_level.iteritems():
    if _val[0] in family_to_members:
        family_to_members[_val[0]].append( (_monster,_val[1]) )
    else:
        family_to_members[_val[0]]=[ (_monster,_val[1]) ]
for _family_name, _family_list in family_to_members.iteritems():
    _family_list.sort(key=lambda x:x[1])
allowable_monster_family_to_members=copy.deepcopy(family_to_members)
del allowable_monster_family_to_members['Fenrir']
del allowable_monster_family_to_members['Tianlung']
del allowable_monster_family_to_members['Plasma']
del allowable_monster_family_to_members['Grippe']

def ffl2standardize(x):
    '''x a string. Standardizes the string for internal usage'''
    y="-"
    z=""
    y2=" "
    x=str.replace(x,y,z)
    x=str.replace(x,y2,z)
    x=str.lower(x)
    x=str.capitalize(x)
    return(x)        

with open(resource_path(os.path.join('data','MonsterStats.txt'))) as f:
    MonsterStats={}
    for line in f:
        line=line.rstrip('\n')
        line=line.split(', ')
        #0=name, 2=hp, 3=str, 4=agi, 5=mana, 6=def, 7..end=abilities
        abilities=[]
        for i in xrange(7,len(line)):
            abilities.append(line.pop(7))
        line.append(abilities)
        #0=name, 2=hp, 3=str, 4=agi, 5=mana, 6=def, 7=abilities
        MonsterStats[ffl2standardize(line[0])] = line[2],line[3],line[4],line[5],line[6],line[7]    

####################################################################################
##Processing functions
####################################################################################

def evolve(monster,meat):
    return EvoDict[monster][meat]


######################################################evolution options calculator
class search_node(object):
    def __init__(self):
        pass
    def __eq__(self,other):
        return self.monster==other.monster and self.normal_index==other.normal_index and self.boss_index==other.boss_index
    def __ne__(self,other):
        return not self==other
    def __hash__(self):
        return hash(self.monster + str(self.normal_index) + str(self.boss_index))
    def __repr__(self):
        return 'SN:'+self.monster+str(self.normal_index) + str(self.boss_index)
def evolution_options(st_monster,maxiter,meats_indices,bossmeats_indices):
    assert len(meats_indices)==12 and len(bossmeats_indices)==12
    meats={}
    for index,val in enumerate(meats_indices):
        if val:
            for meat in noboss_list[index]:
                if meat not in meats:
                    meats[meat]=index #meats[regular meat] = earliest world index available, out of the indices selected
    
    start_node=search_node()
    start_node.monster=st_monster
    start_node.normal_index=-1
    start_node.boss_index=(-1,0) #(world of last boss eaten, index of last boss eaten in that world)

    all_poss=set([start_node])

    def take_min_indices(S):
        '''S a set of search_nodes with monster and index attributes. Updates S in-place'''
        monster_nodes={}
        for node in S:
            monster=node.monster
            if monster in monster_nodes:
                monster_nodes[monster].append(node)
            else:
                monster_nodes[monster]=[node]
        to_cull=[]
        for monster, node_list in monster_nodes.iteritems():
            for M2 in node_list:
                for M1 in node_list:
                    if M1!=M2 and M1.normal_index<=M2.normal_index and M1.boss_index<=M2.boss_index:
                        to_cull.append(M2)
                        #print 'culling',M2
        S.difference_update(to_cull)
            
    done=False
    iters=0
    while not done:
        last_size=len(all_poss)
        new_all_poss=copy.deepcopy(all_poss)
        #print 'nap'
        #for node in new_all_poss:
        #    print node.monster,node.normal_index,node.boss_index
        for monster_node in all_poss:
            monster=monster_node.monster
            for meat in meats:
                new_monster=evolve(monster,meat)
                new_node=search_node()
                new_node.monster=new_monster
                new_node.normal_index=max(meats[meat], monster_node.normal_index)
                new_node.boss_index=monster_node.boss_index
                new_all_poss.add(new_node)
            for world,val in enumerate(bossmeats_indices):
                if val and (world>=monster_node.normal_index): #only eat bosses still available
                    for index_within_world,meat in enumerate(boss_list[world]):
                        if (world,index_within_world)>monster_node.boss_index: #only eat later bosses than the latest boss eaten so far
                            #print 'eating boss', (world,index_within_world)
                            new_monster=evolve(monster,meat)
                            new_node=search_node()
                            new_node.monster=new_monster
                            new_node.normal_index=monster_node.normal_index
                            new_node.boss_index=(world,index_within_world)
                            new_all_poss.add(new_node)
        take_min_indices(new_all_poss)
        all_poss=new_all_poss
        iters+=1
        done = (last_size==len(all_poss)) or (iters>=maxiter)
    #print 'iters',iters
    all_poss=set(x.monster for x in all_poss)
    return all_poss


def evolution_options_old(st_monster,maxiter,meats_set,bossmeats_list): #sometimes erroneously created options that come from eating a later monster, then an earlier boss
    start_node=search_node()
    start_node.monster=st_monster
    start_node.index=-1

    all_poss=set([start_node])

    def take_min_indices(S):
        '''S a set of search_nodes with monster and index attributes'''
        monsters={}
        for node in S:
            monster=node.monster
            if monster in monsters:
                monsters[monster]=min(monsters[monster],node.index)
            else:
                monsters[monster]=node.index
        res=set()
        for monster,index in monsters.iteritems():
            new_node=search_node()
            new_node.monster=monster
            new_node.index=index
            res.add(new_node)
        return res
            
    done=False
    iters=0
    while not done:
        last_size=len(all_poss)
        new_all_poss=copy.copy(all_poss)
        for monster_node in all_poss:
            monster=monster_node.monster
            for meat in meats_set:
                new_monster=evolve(monster,meat)
                new_node=search_node()
                new_node.monster=new_monster
                new_node.index=monster_node.index
                new_all_poss.add(new_node)
            for i,meat in enumerate(bossmeats_list):
                if i>monster_node.index: #only eat later bosses than the latest boss eaten so far
                    new_monster=evolve(monster,meat)
                    new_node=search_node()
                    new_node.monster=new_monster
                    new_node.index=bossmeats_list.index(meat)
                    new_all_poss.add(new_node)
        new_all_poss=take_min_indices(new_all_poss)
        all_poss=new_all_poss
        iters+=1
        done = (last_size==len(all_poss)) or (iters>=maxiter)
    #print 'iters',iters
    all_poss=set(x.monster for x in all_poss)
    return all_poss

#not used anymore
def create_meats(meatsfromworlds=[1],normal_or_boss='normal'):
    if isinstance(meatsfromworlds,int):
        meatsfromworlds=[meatsfromworlds]
    if normal_or_boss=='normal':
        noboss_list=[w1noboss,w2noboss,w3noboss,w4noboss,w5noboss,w6noboss,w7noboss,w8noboss,w9noboss,w10noboss,w11noboss,w12noboss]
        normal_meats=set()
        for k in meatsfromworlds:
            normal_meats.update(noboss_list[k-1])
        return normal_meats
    elif normal_or_boss=='boss':
        boss_list=[w1bosses,w2bosses,w3bosses,w4bosses,w5bosses,w6bosses,w7bosses,w8bosses,w9bosses,w10bosses,w11bosses,w12bosses]
        boss_meats=[]
        for k in meatsfromworlds:
            boss_meats.extend(boss_list[k-1])
        return boss_meats
    else:
        raise ValueError('normal_or_boss must be "normal" or "boss"')

###########################################################path calculator
def is_valid_path(G,P, normal_meats, boss_meats):
    '''P a path in an evolutionary graph G. normal_meats and boss_meats dictionaries mapping meats to indices'''
    pathlen=len(P)
    cur_index=-1
    def discard_meaningless_elts(S):
        '''S a set w/elts of the form (norm_index, (boss_index0, boss_index1)). Updates S in-place'''
        to_cull=set()
        for X in S:
            for Y in S:
                if X[0]>=Y[0] and X[1]>=Y[1] and X!=Y:
                    to_cull.add(X)
        S.difference_update(to_cull)
        

    cur_indices=set([ (-1,(-1,0)) ])
    for i, node in enumerate(P):
        if i+1<pathlen:
            last_indices=copy.copy(cur_indices)
            cur_indices=set()
            
            how=G.get_edge_data(node,P[i+1])['how'] #how to get to the next step

            for meat in how:
                if meat in normal_meats:
                    normal_index=normal_meats[meat]
                    for index in last_indices:
                        cur_indices.add( (max(normal_index,index[0]),index[1]) )
                if meat in boss_meats:
                    boss_index=boss_meats[meat]
                    for index in last_indices:
                        if index[0]<=boss_index[0] and index[1]<boss_index:
                            cur_indices.add( (index[0], boss_index) )
            #print 'ci', cur_indices
            discard_meaningless_elts(cur_indices)
            if len(cur_indices)==0:
                #print 'here', cur_indices
                return False
    return True

def find_paths(start_monster,end_monster,maxiter,meats_indices,bossmeats_indices,return_evo_graph_too=False):
    assert 12==len(meats_indices)==len(bossmeats_indices)
    
    normal_meats={}
    boss_meats={}
    for index, value in enumerate(meats_indices):
        if value:
            for meat in noboss_list[index]:
                if meat not in normal_meats:
                    normal_meats[meat]=index #normal_meats[meat] = index of first world that meat is available in, out of indices selected
    for index, value in enumerate(bossmeats_indices):
        if value:
            for i,meat in enumerate(boss_list[index]): #there is no repetition in boss monsters, fortunately!
                boss_meats[meat]=(index,i) #boss_meats[meat] = (world index, boss index in that world)

    EvoGraph=nx.DiGraph()
    EvoGraph.add_node(start_monster)
    
    #build evolution graph up to maxiter meat-eatings, possibly including invalid paths
    for i in xrange(maxiter):
        new_EvoGraph=copy.deepcopy(EvoGraph)
        for monster in EvoGraph:
            for meat in normal_meats:
                new_monster=evolve(monster,meat)
                ED=new_EvoGraph.get_edge_data(monster,new_monster)
                if ED is None:
                    d={'how':set([meat])}
                else:
                    how=ED['how']
                    how.add(meat)
                    d={'how':how}
                new_EvoGraph.add_edge(monster,new_monster,attr_dict=d)
            for meat in boss_meats: #same exact thing as the "for meat in normal_meats:" block just above
                new_monster=evolve(monster,meat)
                ED=new_EvoGraph.get_edge_data(monster,new_monster)
                if ED is None:
                    d={'how':set([meat])}
                else:
                    how=ED['how']
                    how.add(meat)
                    d={'how':how}
                new_EvoGraph.add_edge(monster,new_monster,attr_dict=d)
        EvoGraph=new_EvoGraph           

    #first find all shortest paths
    valid_paths=[]
    for path in nx.all_shortest_paths(EvoGraph,start_monster,end_monster):
        pathlen=len(path)
        if is_valid_path(EvoGraph,path,normal_meats,boss_meats):
            valid_paths.append(path)

    #if no shortest path is valid, find valid paths of longer length
    if len(valid_paths)==0:
        done= pathlen>maxiter
        while not done:
            pathlen+=1
            for path in nx.all_simple_paths(EvoGraph,start_monster,end_monster,cutoff=pathlen-1):
                if is_valid_path(EvoGraph,path,normal_meats,boss_meats):
                    valid_paths.append(path)
            done=len(valid_paths)>0 or pathlen>maxiter
    if return_evo_graph_too:
        return valid_paths,EvoGraph
    else:
        return valid_paths

def find_paths_of_len_leq(k,start_monster,end_monster,meats_indices,bossmeats_indices,evo_graph): #mostly copy/pasted from find_paths
    assert 12==len(meats_indices)==len(bossmeats_indices)
    
    normal_meats={}
    boss_meats={}
    for index, value in enumerate(meats_indices):
        if value:
            for meat in noboss_list[index]:
                if meat not in normal_meats:
                    normal_meats[meat]=index #normal_meats[meat] = index of first world that meat is available in, out of indices selected
    for index, value in enumerate(bossmeats_indices):
        if value:
            for i,meat in enumerate(boss_list[index]): #there is no repetition in boss monsters, fortunately!
                boss_meats[meat]=(index,i) #boss_meats[meat] = (world index, boss index in that world)

    valid_paths=[]
    for path in nx.all_simple_paths(evo_graph,start_monster,end_monster,cutoff=k):
        if is_valid_path(evo_graph,path, normal_meats,boss_meats):
            valid_paths.append(path)
    return valid_paths

def find_paths_old(start_monster,end_monster,maxiter,meats_set,bossmeats_list,return_evo_graph_too=False):
    '''Finds only valid paths.
        You should only call this if evolution_options says you can get from start_monster to end_monster. Otherwise it may give an exception or return the empty list.
        If return_evo_graph_too is True, returns a tuple: (valid_paths, evolutionary_graph)'''
    EvoGraph=nx.DiGraph()
    EvoGraph.add_node(start_monster)
    meats=set()
    for meat in meats_set:
        meats.add(meat)
    to_pop=[]
    bossmeats_list=copy.copy(bossmeats_list)
    for meat in bossmeats_list:
        meats.add(meat)
        if meat in meats_set:
            to_pop.append(meat)
    for meat in to_pop: #remove
        bossmeats_list.remove(meat)
    #bossmeats_list now consists only of boss meats that cannot be found as normal monster meats.
            
    #build evolution graph up to maxiter meat-eatings, possibly including invalid boss-meat paths
    for i in xrange(maxiter):
        new_EvoGraph=copy.deepcopy(EvoGraph)
        for monster in EvoGraph:
            for meat in meats:
                new_monster=evolve(monster,meat)
                ED=new_EvoGraph.get_edge_data(monster,new_monster)
                if ED is None:
                    d={'how':set([meat])}
                else:
                    how=ED['how']
                    how.add(meat)
                    d={'how':how}
                new_EvoGraph.add_edge(monster,new_monster,attr_dict=d)
        EvoGraph=new_EvoGraph

    #find all valid paths:

    def is_valid_path(G,P):
        '''P a path in G'''
        def exists_nonboss_in_how(S):
            '''S a set'''
            for x in S:
                if x in meats_set:
                    return True
            return False
        pathlen=len(P)
        cur_index=-1
        for i, node in enumerate(P):
            if i+1<pathlen:
                how=G.get_edge_data(node,P[i+1])['how']
                if not exists_nonboss_in_how(how):
                    min_index=min(bossmeats_list.index(x) for x in how)
                    if min_index<=cur_index:
                        return False
                    else:
                        cur_index=min_index
        return True

    #first find all shortest paths
    valid_paths=[]
    for path in nx.all_shortest_paths(EvoGraph,start_monster,end_monster):
        pathlen=len(path)
        if is_valid_path(EvoGraph,path):
            valid_paths.append(path)

    #if no shortest path is valid, find valid paths of longer length
    if len(valid_paths)==0:
        done= pathlen>maxiter
        while not done:
            pathlen+=1
            for path in nx.all_simple_paths(EvoGraph,start_monster,end_monster,cutoff=pathlen-1):
                if is_valid_path(EvoGraph,path):
                    valid_paths.append(path)
            done=len(valid_paths)>0 or pathlen>maxiter

#How to draw a graph
##    G=EvoGraph.subgraph(pathelts)
##    import matplotlib.pyplot
##    d=nx.circular_layout(G)
##    print d
##    nx.draw(G, arrows=False, with_labels=True, pos=d)
##    matplotlib.pyplot.show()

    if return_evo_graph_too:
        return valid_paths,EvoGraph
    else:
        return valid_paths

def find_paths_of_len_leq_old(k,start_monster,end_monster,meats_set,bossmeats_list,evo_graph): #I was a little lazy in writing this. Mostly copy/pasted from find_paths.
    '''Use evo_graph = an output of find_paths. k=# steps.'''
    meats=set()
    for meat in meats_set:
        meats.add(meat)
    to_pop=[]
    bossmeats_list=copy.copy(bossmeats_list)
    for meat in bossmeats_list:
        meats.add(meat)
        if meat in meats_set:
            to_pop.append(meat)
    for meat in to_pop: #remove
        bossmeats_list.remove(meat)
    #bossmeats_list now consists only of boss meats that cannot be found as normal monster meats.

    def is_valid_path(G,P):
        '''P a path in G'''
        def exists_nonboss_in_how(S):
            '''S a set'''
            for x in S:
                if x in meats_set:
                    return True
            return False
        pathlen=len(P)
        cur_index=-1
        for i, node in enumerate(P):
            if i+1<pathlen:
                how=G.get_edge_data(node,P[i+1])['how']
                if not exists_nonboss_in_how(how):
                    min_index=min(bossmeats_list.index(x) for x in how)
                    if min_index<=cur_index:
                        return False
                    else:
                        cur_index=min_index
        return True
    valid_paths=[]
    for path in nx.all_simple_paths(evo_graph,start_monster,end_monster,cutoff=k):
        if is_valid_path(evo_graph,path):
            valid_paths.append(path)
    return valid_paths


def discard_lower_tiers(evolutionoptions):
    '''evolutionoptions a set. Returns a set.'''
    culledevolutionoptions=copy.copy(evolutionoptions)
    for k in evolutionoptions:
        curfamily,curlevel=name_to_family_and_level[k]
        other_family_members=allowable_monster_family_to_members[curfamily] #(monster,level)
        for other in other_family_members:
            if other[0]==k:
                break
            else:
                culledevolutionoptions.discard(other[0])
    return culledevolutionoptions
            
    

class App(object):
    def __init__(self, master, **kwds):
        self.master=master
        self.maxiter=6 #max number of meats to eat in an evolutionary path
        ##########################Status Label 1
        self.StatusLabel1=tk.Label(master,text='No monster selected. Please select a monster to begin.', foreground='red',anchor=tk.W)
        self.StatusLabel1.pack(side=tk.TOP,anchor=tk.W)
        ####################What are you? LabelFrame
        self.WutULabelFrame=tk.LabelFrame(master,text='What are you?')

        self.WutUListBox1Frame=tk.Frame(self.WutULabelFrame)
        self.WutUListBox1Directions=tk.Label(self.WutUListBox1Frame, text='Select family',anchor=tk.W)
        UFamilies=['Flower', 'Obake', 'Fungus', 'Babywyrm', 'Griffon', 'Crab', 'Fiend', 'Jaguar', 'Raven', 'Eagle', 'Woodman', 'Sprite', 'Medusa', 'Toad',
                     'Octopus', 'Zombie', 'Wererat', 'Snake', 'Goblin', 'Silver', 'Fly', 'Skelton', 'Tortoise', 'Worm', 'Lizard', 'Hofud', 'Mapleman', 'Bigeye',
                     'Rhino', 'Moth', 'Slime', 'Spider', 'Beetle', 'Barracud', 'Pebble', 'Babyd']
        PrettyUFamilies=sorted([pretty(s) for s in UFamilies])
        self.WutUListBox1=tk.Listbox(self.WutUListBox1Frame,height=len(UFamilies),width=14,exportselection=False,activestyle='none')
        for item in PrettyUFamilies:
            self.WutUListBox1.insert(tk.END,item)
        self.WutUListBox1.bind("<<ListboxSelect>>",self.on_WutUListBox1_select )

        self.WutUListBox2Frames=[]
        for f in PrettyUFamilies:
            curframe=tk.Frame(self.WutULabelFrame)
            self.WutUListBox2Frames.append(curframe)
            direction=tk.Label(curframe, text='Select monster',anchor=tk.W)
            LB=tk.Listbox(curframe,height=len(allowable_monster_family_to_members[f]),width=14,exportselection=False,activestyle='none')
            for m in allowable_monster_family_to_members[f]:
                LB.insert(tk.END,m[0])
            curframe.LB=LB
            LB.bind("<<ListboxSelect>>",self.on_WutUListBox2_select )
            direction.pack()
            LB.pack()
                
            
        self.WutUListBox1Directions.pack()
        self.WutUListBox1.pack()

        self.WutUListBox1Frame.pack(side=tk.LEFT,anchor=tk.NW)
        self.curWutUListBox2Frame=tk.Frame(self.WutULabelFrame)
        self.curWutUListBox2Frame.LB=tk.Entry(self.curWutUListBox2Frame,width=14, state=tk.DISABLED, bg='light gray')
        direction=tk.Label(self.curWutUListBox2Frame, text='Select monster',anchor=tk.W)
        direction.pack()
        self.curWutUListBox2Frame.LB.pack()
        self.cur_monster=None
        self.curWutUListBox2Frame.pack(side=tk.RIGHT,anchor=tk.NE)

        self.WutULabelFrame.pack(side=tk.LEFT,anchor=tk.NW)
        #########################One step evo box
        self.OneStepLabelFrame=tk.LabelFrame(master, text='One-step evolution')

        OneStepLabel1=tk.Label(self.OneStepLabelFrame, text='What happens if I eat',anchor=tk.W)
        OneStepLabel2=tk.Label(self.OneStepLabelFrame, text='meat? (Type the meat name exactly as it appears in-game)',anchor=tk.W)
        self.OneStepEntryStringVar=tk.StringVar(self.OneStepLabelFrame)
        self.OneStepEntry=tk.Entry(self.OneStepLabelFrame,width=14,textvar=self.OneStepEntryStringVar, state=tk.DISABLED, bg='light gray')
        self.OneStepAnswer=tk.Label(self.OneStepLabelFrame,text='',anchor=tk.W)
        self.OneStepAnswer.pack(side=tk.BOTTOM, anchor=tk.NW)
        OneStepLabel1.pack(side=tk.LEFT)
        self.OneStepEntry.pack(side=tk.LEFT)
        OneStepLabel2.pack(side=tk.LEFT)
        
        self.OneStepEntryStringVar.trace('w',self.on_OneStepEntryType)
        
        self.OneStepLabelFrame.pack(side=tk.TOP,anchor=tk.NW,fill=tk.X)
        ########################Path calculator
        self.PathCalcLabelFrame=tk.LabelFrame(text='Evolution path calculator')

        evo_path_frame=tk.Frame(self.PathCalcLabelFrame)
        directions=tk.Label(evo_path_frame,text='Shortest Paths:')
        directions.pack(anchor=tk.W)
        self.evo_paths=tk.Text(evo_path_frame,height=20,width=40,wrap='none')#,state=tk.DISABLED,bg='black')
        self.evo_paths.pack(fill=tk.BOTH,expand=1)
        evo_path_frame.pack(side=tk.RIGHT,fill=tk.BOTH,expand=1)
        
        directions=tk.Label(self.PathCalcLabelFrame,text='What meats are available? (Select one or more categories)',anchor=tk.W)
        #directions.grid(row=0,column=0, columnspan=2)
        directions.pack(side=tk.TOP,anchor=tk.W)

        

        WorldSelectFrame=tk.Frame(self.PathCalcLabelFrame)
        self.WorldNoBossCheckBoxes=[]
        self.WorldBossCheckBoxes=[]
        self.WorldNoBossCheckBoxVars=[tk.IntVar(self.PathCalcLabelFrame) for k in xrange(12)]
        self.WorldBossCheckBoxVars=[tk.IntVar(self.PathCalcLabelFrame) for k in xrange(12)]
        nobosstxt={1:'W1: First world', 2:"W2: Ashura's world", 3:"W3: Giant's world and inside Ki",
                   4:"W4: Apollo's world", 5:"W5: Guardian's Town", 6:"W6: Venus's city and sewers",
                   7:"W7: Venus's world volcano", 8:"W8: Dragon race world", 9:"W9: Edo",
                   10:"W10: Nasty Dungeon fl 1-5 and Valhalla",
                   11:"W11: Nasty Dunegon fl 6-8 and Final world",
                   12:"W12: Celestial palace"}
        bosstxt={1:'W1 bosses: BabyWyrm, Rhino',
                 2:'W2 bosses: Woodman',
                 3:'W3 bosses: Phagocyt',
                 4:'',
                 5:'W5 bosses: Ogre, Mantcore', 6:'', 7:'',
                 8:'W8 bosses: Adamant, Tortoise, Lamia, Watcher',
                 9:'',
                 10:'W10 bosses: OdinCrow, Sleipnir',
                 11:'',
                 12:'W12 bosses: TianLung, Fenrir'}
        for k in xrange(12):
            cmd=partial(self.on_NoBossCheckBoxPress,k)
            CB=tk.Checkbutton(WorldSelectFrame, text=nobosstxt[k+1], var=self.WorldNoBossCheckBoxVars[k], command=cmd)
            self.WorldNoBossCheckBoxes.append(CB)
            CB.grid(row=k,column=0,sticky=tk.W)

            cmd=partial(self.on_BossCheckBoxPress,k)
            CB=tk.Checkbutton(WorldSelectFrame, text=bosstxt[k+1], var=self.WorldBossCheckBoxVars[k], command=cmd)
            self.WorldNoBossCheckBoxes.append(CB)
            if bosstxt[k+1]!='':
                CB.grid(row=k,column=1,sticky=tk.W)
        WorldSelectFrame.pack(anchor=tk.W)
        directions=tk.Label(self.PathCalcLabelFrame,text='What would you like to become? (Select one and hit "Calculate paths")',anchor=tk.W)
        #directions.grid(row=13,column=0,columnspan=2)
        directions.pack(anchor=tk.W)
        self.evo_options=tk.Listbox(self.PathCalcLabelFrame,exportselection=False,activestyle='none',height=1)
        #self.evo_options.grid(row=14,column=0,columnspan=2,sticky=tk.W)
        self.evo_options.pack(expand=2,fill=tk.BOTH)
        self.CalcPathsButton=tk.Button(self.PathCalcLabelFrame,text='Calculate paths',command=self.compute_and_populate_paths)
        #self.CalcPathsButton.grid(row=15,column=0,columnspan=2,sticky=tk.W+tk.E)
        self.CalcPathsButton.pack()
        self.evo_options.bind("<Return>",self.compute_and_populate_paths)
        self.evo_options.bind("<Double-Button-1>",self.compute_and_populate_paths)

        
        
        self.PathCalcLabelFrame.pack(side=tk.LEFT,anchor=tk.NW,fill=tk.BOTH,expand=1)
    def on_NoBossCheckBoxPress(self,i):
        #if not self.WorldNoBossCheckBoxVars[i].get():
        #    self.WorldBossCheckBoxVars[i].set(0)
        self.compute_and_populate_evo_options()
    def on_BossCheckBoxPress(self,i):
        if True: #i<11:
            if self.WorldBossCheckBoxVars[i].get():
                self.WorldNoBossCheckBoxVars[i].set(1)
        self.compute_and_populate_evo_options()
##    def _compute_noboss_meats(self):
##        noboss_worlds=[]
##        for i,V in enumerate(self.WorldNoBossCheckBoxVars):
##            if V.get():
##                noboss_worlds.append(i+1)
##        noboss_meats=create_meats(meatsfromworlds=noboss_worlds,normal_or_boss='normal')
##        return noboss_meats
##    def _compute_boss_meats(self):
##        boss_worlds=[]
##        for i,V in enumerate(self.WorldBossCheckBoxVars):
##            if V.get():
##                boss_worlds.append(i+1)
##        boss_meats=create_meats(meatsfromworlds=boss_worlds,normal_or_boss='boss')
##        return boss_meats
    def _get_noboss_meats_indices(self):
        res=[x.get() for x in self.WorldNoBossCheckBoxVars]
        return res
    def _get_boss_meats_indices(self):
        res=[x.get() for x in self.WorldBossCheckBoxVars]
        return res
        
    def compute_and_populate_evo_options(self):
        noboss_indices=self._get_noboss_meats_indices()
        boss_indices=self._get_boss_meats_indices()

        if self.cur_monster is not None:
            EO=evolution_options(st_monster=self.cur_monster, maxiter=self.maxiter, meats_indices=noboss_indices,bossmeats_indices=boss_indices)
            #EO=evolution_options(self.cur_monster,maxiter=self.maxiter,meats_set=noboss_meats,bossmeats_list=boss_meats)
            EO=discard_lower_tiers( EO )
            EO.discard(self.cur_monster)
            EO=list(EO)
            EO.sort()
            self.evo_options.delete(0,tk.END)
            for monster in EO:
                self.evo_options.insert(tk.END,monster+' '+self.prettify_monsterstats(MonsterStats[monster]))
                
    def compute_and_populate_paths(self,*args):
        if self.cur_monster is not None:
            try:
                target=self.evo_options.get( self.evo_options.curselection()[0] )
                target=target.split(' (')[0]
                contin=True
            except IndexError:
                contin=False
            if contin:
                self.evo_paths.delete(1.0,tk.END)
                noboss_meats_indices=self._get_noboss_meats_indices()
                boss_meats_indices=self._get_boss_meats_indices()
                P,G=find_paths(start_monster=self.cur_monster,end_monster=target,
                               maxiter=self.maxiter,meats_indices=noboss_meats_indices,bossmeats_indices=boss_meats_indices,return_evo_graph_too=True)
                #P,G=find_paths(self.cur_monster,target,self.maxiter,noboss_meats,boss_meats,True)
                if len(P[0])<4:   
                    for path in find_paths_of_len_leq(3,self.cur_monster,target,noboss_meats_indices,boss_meats_indices,G):
                        if path not in P:
                            P.append(path)
                    P.sort(key=lambda x:-len(x))
                def set_to_pretty_str(S):
                    S=list(S)
                    S.sort()
                    s=str(S)
                    s=s.replace(', ',' or ')
                    s=s.replace("'",'')
                    if len(S)==1:
                        s=s.replace('[','')
                        s=s.replace(']','')            
                    return s
                for p in P:
                    this_path=''#'Path:\n'
                    pathlen=len(p)
                    for i,a in enumerate(p):
                        if i<pathlen-1:
                            b=p[i+1]
                            this_path+= a+' + '+set_to_pretty_str(G.get_edge_data(a,b)['how'])+' = '+b+' '+self.prettify_monsterstats(MonsterStats[b])+'\n'
                    this_path+='\n'
                    self.evo_paths.insert(1.0,this_path)
                                
    def on_WutUListBox1_select(self, event):
        i=self.WutUListBox1.curselection()
        self.curWutUListBox2Frame.pack_forget()
        try:
            oldsel=self.curWutUListBox2Frame.LB.curselection()[0]
            self.curWutUListBox2Frame.LB.selection_clear(oldsel)
        except:# IndexError:
            pass
        self.curWutUListBox2Frame=self.WutUListBox2Frames[i[0]]
        self.curWutUListBox2Frame.pack(side=tk.RIGHT,anchor=tk.NE)
    def on_WutUListBox2_select(self,event):
        W=event.widget
        self.cur_monster=W.get(W.curselection()[0])
        self.StatusLabel1.config(text='Current monster selected: '+self.cur_monster, foreground='black')
        self.OneStepEntry.config(state=tk.NORMAL,bg='white')
        self.on_OneStepEntryType()
        self.compute_and_populate_evo_options()
        self.master.wm_title(self.cur_monster+" evolution options")
    def on_OneStepEntryType(self,*args):
        input_=ffl2standardize(self.OneStepEntryStringVar.get())
        try:
            result=evolve(self.cur_monster,input_)
        except:
            result=None
        if result is None:
            self.OneStepAnswer.config(text='')
        else:
            self.OneStepAnswer.config(text='Answer: '+self.cur_monster+' + '+input_+' = '+result+' '+self.prettify_monsterstats(MonsterStats[result]))
    def prettify_monsterstats(self,T):
        hp,strength,agi,mana,defense,abilities=T
        res='('+hp+' HP, '+strength+' str, '+defense+' def, '+agi+' agi, '+mana+' mana, '
        for ability in abilities:
            res+=ability+', '
        res=res.rstrip(', ')
        res=res+')'
        return res
####################################################################################TESTING

if 0:
    def set_to_pretty_str(S):
        S=list(S)
        S.sort()
        s=str(S)
        s=s.replace(', ',' or ')
        s=s.replace("'",'')
        if len(S)==1:
            s=s.replace('[','')
            s=s.replace(']','')            
        return s
    #P,G=find_paths('Starterbabyd','Cameleon',7,['Rhino','Jaguar'],['Fly'],True)
    P,G=find_paths('Starterbabyd','Cameleon',5,w1noboss,w1bosses,True)
    for p in P:
        print 'path:'
        pathlen=len(p)
        for i,a in enumerate(p):
            if i<pathlen-1:
                b=p[i+1]
                print a,'+',set_to_pretty_str(G.get_edge_data(a,b)['how']),'=',b,MonsterStats[b]
                print ''
        print ''



        


##to_pretty={'OBake':'O-Bake (Ghost)',
##           'Babywyrm':'BabyWyrm',
##           'Wererat':'WereRat',
##           'Woodman':'WoodMan (Golem)',
##           'Mapleman':'MapleMan (Treant)',
##           'Bigeye':'Big-Eye',
##           'Hofud':'Hofud (Sword)',
##           'Babyd':'Dragon'}           
def pretty(s):
    return s
    if s in to_pretty:
        return to_pretty[s]
    return s    


#############################################################Run app    
if 1:

    
    root=tk.Tk()
    root.wm_title('FFL2 Monster Evolution Path Calculator: Select your monster')
##    Photo=Image.open('jaguar.png')
##    Photo.thumbnail((24,24))
##    Photo=PhotoImage(Photo)
##    B=tk.Button(root,image=Photo)
##    B.pack()

    A=App(root)

#    root.update()
#    print root.geometry()

    
    tk.mainloop()

if 0:
    P=find_paths('Babyd','Ogre',3,meats_indices=[0,0,0,0,1,1,0,0,0,0,0,0,],bossmeats_indices=[0,0,0,0,1,0,0,0,0,0,0,0],return_evo_graph_too=False)
    print P

        
