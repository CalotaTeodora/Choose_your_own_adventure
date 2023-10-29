# Choose Your One Adventure

Welcome to **Choose Your One Adventure**, an interactive text-based adventure game where you guide a traveler named Elara through the mystical Whispering Woods. In this game, you control the story by making choices, leading Elara to success or peril. Your decisions shape the narrative, and every choice matters.

## How to Play

1. **Starting the Game:**
   - The game begins with Elara on a quest to find the lost Gem of Serenity in the Whispering Woods.
   - You, the player, are the guide. Start by selecting weapons for Elara to use. Choose wisely; her fate depends on it.

2. **Making Choices:**
   - Navigate the story by making decisions for Elara.
   - Explore different paths, some leading to success and others to unfortunate endings.
   - Be cautious! Wrong choices might lead to Elara's demise.

3. **Rules:**
   - Follow the provided template to maintain the story's flow.
   - Ensure that death scenarios include a descriptive explanation, ending with the text: "The End."
   - Create branching narratives with diverse outcomes based on player choices.

## How the Game Works

- **Chat History:** The game remembers your choices and the unfolding story. Your previous interactions influence the narrative, so pay attention to the chat history provided.
  
- **Interactive Dialogue:** Use the `Your reply:` prompt to input Elara's actions and decisions.
  
- **Branching Narratives:** The story adapts based on your choices, leading to different story arcs and endings.

## Getting Started

1. **Setup Cassandra Database:**
   - Configure your Cassandra database using the provided `cloud_config` and secrets from `choose_your_one_adventure-token.json`.

2. **OpenAI Integration:**
   - Use OpenAI's language model to generate dynamic and engaging responses for the game.
   - The `llm_chain` interacts with the Cassandra chat history and your inputs to create the story.

3. **Play the Game:**
   - Run the Python script to start the game.
   - Follow the prompts to make choices for Elara.
   - Explore different paths and uncover the fate of Elara in the Whispering Woods.

## Customize Your Adventure

- **Modify the Template:** Adjust the game's template to create new scenarios and dialogues.
  
- **Extend the Story:** Add more paths, challenges, and characters to expand the adventure.

- **Enhance Gameplay:** Implement new features, such as inventory systems or character progression, to enhance the player experience.

## Contribute

- **Report Issues:** Found a bug or have a suggestion? [Create an issue]([link to issues](https://github.com/CalotaTeodora/Choose_your_own_adventure/issues/1)) and let us know!
  
- **Contribute Code:** Want to add new features or fix existing issues? Fork the repository, make your changes, and create a pull request.

## Credits

This game is developed using Python, Cassandra, and OpenAI by [CalotaTeodora]. Inspired by classic text-based adventures, it offers a modern and interactive storytelling experience.

Enjoy your journey in the Whispering Woods! Remember, every choice you make shapes Elara's destiny.

---

**Note:** This README provides an overview of the game. For detailed setup instructions and technical information, please refer to the documentation and comments within the code files.
