# TI101I - Hogwarts Project: The Art of Coding like a Wizard
An interactive python text-based adventure game set in the Harry Potter universe, where players experience their first year at Hogwarts School of Witchcraft and Wizardry! The game includes character creation, house sorting, spell learning, and a Quidditch match simulation.

The adventure is divided into four chapters:
- **Chapter I**: Fall into the Magical World
- **Chapter II**: Friends, Foes, and the Sorting Hat
- **Chapter III**: Wand, words, and wonders
- **Chapter IV**: The Chase of the Golden Snitch

## 👥 Contributors
Ines Maatoug & Anas Hamdi, Int-3

## Installation

### ╰୧ Prerequisites
- Python 3.x installed on your system
- Git installed

### Clone the Repository
```bash
git clone https://github.com/[your-username]/hogwarts-[student1name]-[student2name]-[groupname].git
cd hogwarts-[student1name]-[student2name]-[groupname]
```

## ╰୧ Usage

### ⟣．． Running the Game

From the project root directory, run:
```bash
python main.py
```

Or:
```bash
python3 main.py
```
### ⟣．． Gameplay Instructions

#### Follow these not to get expelled from Hogwarts!
1. **Start the game** - Choose "Yes" when prompted
2. **Accept the letter** - Choose to go to Hogwarts
3. **Shopping** - Buy required items (Magic Wand, Wizard Robe, Potions Book) and choose a pet

#### Examples of commands or use cases

   **Starting the game:**
```
$ python main.py
[Hogwarts ASCII art appears]
Do you want to start your adventure?
1. Yes
2. No, exit the game
Your choice: 1
```

   **Character creation example:**
```
Write your last name on the ticket: Deight
Write your first name on the ticket: Erza

How brave are you when facing the unknown? (1-10): 6
How sharp is your mind? (1-10): 7
How loyal are you to those you care about? (1-10): 4
How determined are you to achieve your goals? (1-10): 9
```

   **Shopping example:**
```
You have 100 Galleons.
Catalog of available items:
1. Magic Wand - 35 Galleons (required)
2. Wizard Robe - 20 Galleons (required)
3. Tin Cauldron - 15 Galleons
4. Potions Book - 25 Galleons (required)
...

Enter the number of the item to buy: 1
You bought: Magic Wand (-35 Galleons).
You have 65 Galleons.
```


### ⟣．． Game Controls

- **Text input**: Type your answers and press Enter
- **Number input**: Enter numbers within the specified range
- **Multiple choice**: Enter the number corresponding to your choice
- **Continue**: Press Enter when prompted to advance the story

## ╰୧ Key Features

### ⟣．． Custom character creation
- First and last name
- Four attributes: Courage, Intelligence, Loyalty, and Ambition
- Inventory management (items and spells)
- Money system (Galleons)

### ⟣．． House System
- Four Hogwarts houses: Gryffindor, Slytherin, Hufflepuff, Ravenclaw
- Sorting algorithm based on attributes and personality quiz
- House points tracking throughout the game

### ⟣．． Interactive Gameplay
- Dynamic narrative that responds to player choices
- Character interactions that affect attributes
- Strategic shopping with budget management
- Random spell selection for personalized experience
- Random Quidditch match opponents

## ╰୧ Logbook

### ⟣．． Project Timeline

#### Week 1: November 28 - December 2, 2025
**Milestone**: Project initialization and input utilities

**Work completed:**
- Set up project structure and repository
- Implemented input validation system (`utils/input_utils.py`)
- Created functions for text, number, and choice inputs with manual integer conversion

**Key milestones:**
- Project repository created
- Basic input validation complete

---

#### Week 2: December 11-18, 2025
**Milestone**: Core game systems (Character and House modules)

**Work completed:**
- Implemented character management system (`universe/character.py`)
- Developed house point tracking and sorting algorithm (`universe/house.py`)

**Problems encountered:**

- `assign_house()` had indexing bug (0-based vs 1-based)
- Solution: Adjusted `ask_number()` range and array indexing

**Key milestones:**
- Character system functional
- House sorting algorithm working

---

#### Week 3: December 19-21, 2025
**Milestone**: Chapters 1-3 complete (Intermediate Submission)

**Work completed:**
- Chapter 1: Character creation, Hogwarts letter, Diagon Alley shopping
- Chapter 2: Train journey, Sorting Ceremony, common room entrance
- Chapter 3: Spell learning and magic quiz
- Menu system and main game loop

**Decisions made:**
- Chose narrative-heavy approach with extensive atmospheric details
- Integrated ASCII art at key moments for visual impact
- Added pet sounds based on player choice for immersion
- Created Professor-specific personalities (Flitwick vs. Snape)
- Designed unique house entrance descriptions
- Used emoji indicators for spell types (⚔️🛡️✨)

**Key milestones:**
- Intermediate submission completed December 21
- All three chapters fully functional
- Core gameplay loop established

---

#### Week 4: January 2, 2026
**Milestone**: Chapter 4 and Final Submission

**Work completed:**
- Implemented complete Quidditch match system with 8 functions
- Added team creation, goal mechanics, Golden Snitch system
- Created dramatic narrative framing for match
- Final testing and bug fixes across all modules
- Completed README documentation

**Decisions made:**
- Created different victory/defeat narratives
- Included celebratory/consoling messages based on outcomes

**Key milestones:**
- Final submission completed January 2
- Full game tested and validated

---

### ⟣．． Task Distribution

Ines Maatoug (7nies): Mainly wrote the narrative text and did the ascii art. Helped with the functions
Anas Hamdi: Coded the functions.


## 🧪 Testing & Validation

### ⟣．． Input Validation
The game includes robust input validation:
- **Text inputs**: Cannot be empty or whitespace-only
- **Number inputs**: Must be integers within specified ranges
- **Budget checking**: Ensures player has enough money before purchases
- **Required items**: Verifies all mandatory items are purchased before proceeding

### ⟣．． Known Issues
- None currently 

___

**"It is our choices that show what we truly are, far more than our abilities."** - Albus Dumbledore