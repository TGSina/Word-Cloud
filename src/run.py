from wordcloud import WordCloud
import matplotlib.pyplot as plt

class WordCloudGenerator:
    def __init__(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            self.text = file.read()

    def run(self, output_path=None):
        if output_path:
            self.generate_wordcloud(output_path)
        else:
            self.display_wordcloud()

    def generate_wordcloud(self, output_path):
        """Generates a word cloud and saves it to the specified output path."""
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(self.text)
        wordcloud.to_file(output_path)

    def display_wordcloud(self):
        """Generates a word cloud and saves it to the specified output path."""
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(self.text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
        
    # Another method to run:
    def run_now(self, output_path: str, **kwargs) -> None:
        """
        Generate a word cloud image.

        :param output_path: The path to the output file.
        """
        WordCloud(**kwargs).generate(self.text).to_file(output_path)


if __name__ == "__main__":
    movies_wordcloud = WordCloudGenerator('data/movies.txt')
    movies_wordcloud.run()  # Display the word cloud
    # Uncomment the line below to save the word cloud to a file
    movies_wordcloud.run('output/movies_wordcloud.png')  # Save the word cloud to a file

