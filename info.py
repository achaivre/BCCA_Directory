# IMPORTS
from dataclasses import dataclass
# -------- DATACLASS ------------

@dataclass
class Cohort:
  fname: str
  lname: str
  pronouns: str
  age: int
  email: str
  aboutme: str
  funfact: str
  fullname: str
# Below is how we make our class print as expected in the console.
  def __repr__(self) -> str:
    return '''Name: {} {} 
Pronouns: {}
Age: {}
Email: {}
About Me: {}
Fun Fact: {}'''.format(self.fname, self.lname, self.pronouns, self.age, self.email, self.aboutme, self.funfact)


# ------------ DEFINED VARIABLES FOR COHORT MEMBERS --------

mem1 = Cohort('Armando', 'Quiñonez', 'he/him', 24, 'aquinonez@basecampcodingacademy.org', 'https://tinyurl.com/armandoq',"He plays the guitar. 🏜️", 'Armando Quiñonez')

mem2 = Cohort('Luis', 'Ortiz', 'he/him', 25, 'lortiz@basecampcodingacademy.org', 'https://tinyurl.com/lortiz', 'He repairs guitars. 🧰', 'Luis Ortiz')

mem3 = Cohort('Alyx', 'Chaivre', 'she/her', 27, 'achaivre@basecampcodingacademy.org', 'https://tinyurl.com/achaivre', 'Her name came from a tawdry romance novel. 🤯', 'Alyx Chaivre')

mem4 = Cohort('Ashley', 'Glasz', 'she/her', 32, 'aglasz@basecampcodingacademy.org', 'https://tinyurl.com/aglasz', 'She is a graphic designer. 🖌️', 'Ashley Glasz')

mem5 = Cohort('Lucas', 'Dickerson', 'they/them', 24, 'ldickerson@basecampcodingacademy.org', 'https://tinyurl.com/ldickerson', 'They are an artist with a commission business! Check them out! 🖌', "Lucas Dickerson")

mem6 = Cohort('John', 'Person', 'he/him', 55, 'jperson@basecampcodingacademy.org', 'https://tinyurl.com/jperson1', 'He enjoys a nice picture. 	🏔', "John Person")

mem7 = Cohort('Patrick', 'Petit', 'he/him', 39, 'ppetit@basecampcodingacademy.org', 'https://tinyurl.com/ppetit4', 'He was in a band! (With another cohort member!) 🥁', "Patrick Petit" )

mem8 = Cohort('Drew', 'Cornelius', 'he/him', 25, 'dcornelius@basecampcodingacademy.org', 'https://tinyurl.com/dcornelius', 'He has traveled all over the world. 🤠', 'Drew Cornelius')

mem9 = Cohort('Eddie', 'Rosas', 'he/him', 30, 'erosas@basecampcodingacademy.org', 'https://tinyurl.com/erosas1', 'He can cook! (It tastes really good... Like for real.)👨🏽‍🍳', 'Eddie Rosas')

mem10 = Cohort('Laura', 'Hackman', 'she/her', 37, 'lhackman@basecampcodingacademy.org', 'https://tinyurl.com/lhackman1', 'She makes her own costumes from scratch! ✈️', 'Laura Hackman')

mem11 = Cohort('Anna', 'Lacy', 'she/her', 30, 'alacy@basecampcodingacademy.org', 'https://tinyurl.com/alacy1', 'She can paint! She does great art! ✍', 'Anna Lacy')
    
mem12 = Cohort('Logan', 'Floyd', 'he/him', 29, 'lfloyd@basecampcodingacademy.org', 'https://tinyurl.com/lfloyd2', "He plays guitar! 🎸", 'Logan Floyd')

mem13 = Cohort('Anthony', 'Williams', 'he/him', 31, 'awilliams@basecampcodingacademy.org', 'https://tinyurl.com/awilliams2', 'He has a degree in psychology! 📔','Anthony Williams')

mem14 = Cohort('Joseph', 'Dunn', 'he/him', 23, 'jdunn@basecampcodingacademy.org', 'https://tinyurl.com/jdunn2', 'He owns a Phantom Fire Studios! 👮','Joseph Dunn')

mem15 = Cohort('Conner', 'Gray', 'he/him', 23, 'cgray@basecampcodingacademy.org', 'https://tinyurl.com/cgray6', 'He is the code. 🤖','Conner Gray' )

mem16 = Cohort('Jarvis', 'Pettis', 'he/him', 25, 'jpettis@basecampcodingacademy.org', 'https://tinyurl.com/jpettis1', 'He is a brick mason. 🧱', 'Jarvis Pettis')

mem17 = Cohort('Jacob', 'Padgett', 'he/him', 27, 'jpadgett@basecampcodingacademy.org', 'https://tinyurl.com/jpadgett1', 'He can fight a mountain lion with his bare hands. 🦁', 'Jacob Padgett')

mem18 = Cohort('Beckett', 'Padgett', 'he/him', 25, 'bpadgett@basecampcodingacademy.org', 'https://tinyurl.com/bpadgett1', 'He likes numbers 767-25-7997. 👾', 'Beckett Padgett')

mem19 = Cohort('Tyler', 'Allen', 'he/him', 23, 'tallen@basecampcodingacademy.org', 'https://tinyurl.com/tallen1', 'He is an avid reader! (He wants to help robots take over the planet). 🦿', 'Tyler Allen')

mem20 = Cohort('Bryan', 'Mcmurry', 'he/him', 31, 'bmcmurry@basecampcodingacademy.org', 'https://tinyurl.com/bmcmurry1', 'He knows Brazilian Jiu-Jitsu! 🥋', 'Bryan Mcmurry')

mem21 = Cohort('Phillip', 'Mardis', 'he/him', 40, 'pmardis@basecampcodingacademy.org', 'https://tinyurl.com/pmardis1', 'He was in a band! (With another cohort member!) 👨‍🦲', 'Phillip Mardis')

mem22 = Cohort('Julia', 'Luna', 'she/her', 41, 'jluna@basecampcodingacademy.org', 'https://tinyurl.com/jluna1', 'She has a degree in Art! 🏵', 'Julia Luna')

mem23 = Cohort('Lee', 'Egdorf', 'he/him', 23, 'legdorf@basecampcodingacademy.org', 'https://tinyurl.com/legdorf1', 'He has experience in a few technical languages! 🐉 ', 'Lee Egdorf')

mem24 = Cohort('Cameron', 'Fortner', 'she/her', 23, 'cfortner1@basecampcodingacademy.org', 'https://tinyurl.com/cfortner', 'She enjoys drawing! 🖼️', 'Cameron Fortner')

mem25 = Cohort('Joe', 'Trott', 'he/him', 22, 'jtrott@basecampcodingacademy.org', 'https://tinyurl.com/jtrott', 'He enjoys drawing! 🌶', 'Joe Trott')

mem26 = Cohort('Nathan', 'Moss', 'he/him', 24, 'nmoss@basecampcodingacademy.org', 'https://tinyurl.com/nmoss3', 'He makes models as a hobby! 🎺', 'Nathan Moss')

# - Overall Cohort Data -

cohort_data = [mem1, mem2, mem3, mem4, mem5, mem6,mem7, mem8, mem9, mem10, mem11, mem12, mem13, mem14, mem15, mem16, mem17, mem18, mem19, mem20, mem21, mem22, mem23, mem24, mem25, mem26]

# - Overall Cohort First Name List -
cohort_fnames = [mem1.fname, mem2.fname, mem3.fname, mem4.fname, mem5.fname, mem6.fname, mem7.fname, mem8.fname, mem9.fname, mem10.fname, mem11.fname, mem12.fname, mem13.fname, mem14.fname, mem15.fname, mem16.fname, mem17.fname, mem18.fname, mem19.fname, mem20.fname, mem21.fname, mem22.fname, mem23.fname, mem24.fname, mem25.fname, mem26.fname]

# - Overall Cohort Last Name List - 
cohort_lnames = [mem1.lname, mem2.lname, mem3.lname, mem4.lname, mem5.lname, mem6.lname, mem7.lname, mem8.lname, mem9.lname, mem10.lname, mem11.lname, mem12.lname, mem13.lname, mem14.lname, mem15.lname, mem16.lname, mem17.lname, mem18.lname, mem19.lname, mem20.lname, mem21.lname, mem22.lname, mem23.lname, mem24.lname, mem25.lname, mem26.lname]

# - Overall Cohort Full Name List -

cohort_fullnames = [mem1.fullname, mem2.fullname, mem3.fullname, mem4.fullname, mem5.fullname, mem6.fullname, mem7.fullname, mem8.fullname, mem9.fullname, mem10.fullname, mem11.fullname, mem12.fullname, mem13.fullname, mem14.fullname, mem15.fullname, mem16.fullname, mem17.fullname, mem18.fullname, mem19.fullname, mem20.fullname, mem21.fullname, mem22.fullname, mem23.fullname, mem24.fullname, mem25.fullname, mem26.fullname]

