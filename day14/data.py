from typing import List
from dataclasses import dataclass

@dataclass
class Data():
    name: str
    follower_count: int
    description: str
    country: str

data: List[Data] = [
    Data(name='Instagram', follower_count=346, description='Social media platform', country='United States'),
    Data(name='Cristiano Ronaldo', follower_count=215, description='Footballer', country='Portugal'),
    Data(name='Ariana Grande', follower_count=183, description='Musician and actress', country='United States'),
    Data(name='Dwayne Johnson', follower_count=181, description='Actor and professional wrestler', country='United States'),
    Data(name='Selena Gomez', follower_count=174, description='Musician and actress', country='United States'),
    Data(name='Kylie Jenner', follower_count=172, description='Reality TV personality and businesswoman and Self-Made Billionaire', country='United States'),
    Data(name='Kim Kardashian', follower_count=167, description='Reality TV personality and businesswoman', country='United States'),
    Data(name='Lionel Messi', follower_count=149, description='Footballer', country='Argentina'),
    Data(name='Beyoncé', follower_count=145, description='Musician', country='United States'),
    Data(name='Neymar', follower_count=138, description='Footballer', country='Brasil'),
    Data(name='National Geographic', follower_count=135, description='Magazine', country='United States'),
    Data(name='Justin Bieber', follower_count=133, description='Musician', country='Canada'),
    Data(name='Taylor Swift', follower_count=131, description='Musician', country='United States'),
    Data(name='Kendall Jenner', follower_count=127, description='Reality TV personality and Model', country='United States'),
    Data(name='Jennifer Lopez', follower_count=119, description='Musician and actress', country='United States'),
    Data(name='Nicki Minaj', follower_count=113, description='Musician', country='Trinidad and Tobago'),
    Data(name='Nike', follower_count=109, description='Sportswear multinational', country='United States'),
    Data(name='Khloé Kardashian', follower_count=108, description='Reality TV personality and businesswoman', country='United States'),
    Data(name='Miley Cyrus', follower_count=107, description='Musician and actress', country='United States'),
    Data(name='Katy Perry', follower_count=94, description='Musician', country='United States'),
    Data(name='Kourtney Kardashian', follower_count=90, description='Reality TV personality', country='United States'),
    Data(name='Kevin Hart', follower_count=89, description='Comedian and actor', country='United States'),
    Data(name='Ellen DeGeneres', follower_count=87, description='Comedian', country='United States'),
    Data(name='Real Madrid CF', follower_count=86, description='Football club', country='Spain'),
    Data(name='FC Barcelona', follower_count=85, description='Football club', country='Spain'),
    Data(name='Rihanna', follower_count=81, description='Musician and businesswoman', country='Barbados'),
    Data(name='Demi Lovato', follower_count=80, description='Musician and actress', country='United States'),
    Data(name="Victoria's Secret", follower_count=69, description='Lingerie brand', country='United States'),
    Data(name='Zendaya', follower_count=68, description='Actress and musician', country='United States'),
    Data(name='Shakira', follower_count=66, description='Musician', country='Colombia'),
    Data(name='Drake', follower_count=65, description='Musician', country='Canada'),
    Data(name='Chris Brown', follower_count=64, description='Musician', country='United States'),
    Data(name='LeBron James', follower_count=63, description='Basketball player', country='United States'),
    Data(name='Vin Diesel', follower_count=62, description='Actor', country='United States'),
    Data(name='Cardi B', follower_count=67, description='Musician', country='United States'),
    Data(name='David Beckham', follower_count=82, description='Footballer', country='United Kingdom'),
    Data(name='Billie Eilish', follower_count=61, description='Musician', country='United States'),
    Data(name='Justin Timberlake', follower_count=59, description='Musician and actor', country='United States'),
    Data(name='UEFA Champions League', follower_count=58, description='Club football competition', country='Europe'),
    Data(name='NASA', follower_count=56, description='Space agency', country='United States'),
    Data(name='Emma Watson', follower_count=56, description='Actress', country='United Kingdom'),
    Data(name='Shawn Mendes', follower_count=57, description='Musician', country='Canada'),
    Data(name='Virat Kohli', follower_count=55, description='Cricketer', country='India'),
    Data(name='Gigi Hadid', follower_count=54, description='Model', country='United States'),
    Data(name='Priyanka Chopra Jonas', follower_count=53, description='Actress and musician', country='India'),
    Data(name='9GAG', follower_count=52, description='Social media platform', country='China'),
    Data(name='Ronaldinho', follower_count=51, description='Footballer', country='Brasil'),
    Data(name='Maluma', follower_count=50, description='Musician', country='Colombia'),
    Data(name='Camila Cabello', follower_count=49, description='Musician', country='Cuba'),
    Data(name='NBA', follower_count=47, description='Club Basketball Competition', country='United States')
]

