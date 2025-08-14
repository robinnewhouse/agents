#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from ghost_writer.crew import GhostWriter

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    
    idea = """
Write an epic, surreal, and exuberant novel chronicling the first-ever Burning Man held on the Moon, blending the 
spirit of radical self-expression with hard science and speculative culture.

The story follows a diverse cast—astronaut artists, lunar engineers, techno shamans, and cosmic DJs—who converge 
at Mare Serenitatis for a weeklong festival unlike anything humanity has ever attempted. Camps sprawl across 
regolith dunes. Lunar rovers tow mobile sound stages. Low-gravity dance parties erupt in slow-motion euphoria. 
Massive reflective sculptures catch Earthrise, turning each dawn into a transcendent ritual.

As the festival progresses, logistical challenges—life support glitches, dust storms, fuel shortages—force the 
community to work together, highlighting radical interdependence. Meanwhile, an enigmatic artifact is discovered 
beneath the festival grounds: a buried monolith emitting faint signals that sync perfectly with the festival’s 
music and heartbeat.

Themes to explore include:
- Radical community beyond Earth: How do Burning Man’s principles adapt when survival literally depends on 
  collaboration?
- Art as exploration: How does creative expression redefine humanity’s relationship with the Moon?
- Frontier spirituality: How do participants reconcile the sacred and the absurd in a place where humans were 
  never meant to exist?
- Earth nostalgia: As festival-goers look back at the blue marble floating in space, what new perspective on 
  home and belonging emerges?

The tone is wild, kinetic, and luminous, capturing both the sensory overload of a lunar carnival and the quiet awe 
of standing on another world. Prose should weave together technical detail (habitats, suits, rovers) with ecstatic, 
poetic descriptions of lunar raves, microgravity art, and silent sunrise meditations on the regolith.

Let the novel celebrate the joy, absurdity, and fierce hope of building community—even on the Moon—and explore what 
it means to bring the fire of human culture to the cold, ancient surface of another world.
"""

    inputs = {
        'idea': idea,
        'author': 'Morgan Vale',
        'title': 'Tactile Reveries: Meditations on Absence and Presence'
    }
    
    try:
        GhostWriter().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
