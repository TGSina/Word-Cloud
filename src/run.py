from wordcloud import WordCloud
import arabic_reshaper
from bidi.algorithm import get_display
import matplotlib.pyplot as plt

class WordCloudGenerator:
    def __init__(self, file_path, if_rtl=False):
        """
        Initializes the WordCloudGenerator with the text from the specified file.
        :param file_path: Path to the text file containing the words for the word cloud.
        :param if_rtl: Boolean indicating if the text is right-to-left (default is False).
        """
        self.if_rtl = if_rtl
        if if_rtl:
            # Read the Persian text file
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            # Reshape and reorder the text for proper display
            reshaped_text = arabic_reshaper.reshape(text)
            bidi_text = get_display(reshaped_text)
            self.text = bidi_text
        else:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.text = file.read()

    def run(self, output_path=None):
        if self.if_rtl:
            # Original stopwords list
            raw_stopwords = ['و', 'در', 'به', 'های', 'از', 'با', 'بی', 'را', 'برای', 'دو', 'می', 'ها', 'یک', 'بر', 'هم']
            # Preprocess stopwords
            reshaped_stopwords = [arabic_reshaper.reshape(word) for word in raw_stopwords]
            bidi_stopwords = {get_display(word) for word in reshaped_stopwords}

            wordcloud = WordCloud(
                font_path='fonts/bnazanin.ttf',  # Specify the path to your Persian font
                width=800,
                height=400,
                background_color='white',
                stopwords=bidi_stopwords,
                ).generate(self.text)
        else:
            wordcloud = WordCloud(
                width=800,
                height=400,
                background_color='white'
            ).generate(self.text)

        if output_path:
            wordcloud.to_file(output_path)
        else:
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.show()


    # def generate_wordcloud(self, output_path):
    #     """Generates a word cloud and saves it to the specified output path."""

    #     wordcloud.to_file(output_path)

    # def display_wordcloud(self):
    #     """Generates a word cloud and saves it to the specified output path."""

    #     plt.figure(figsize=(10, 5))
    #     plt.imshow(wordcloud, interpolation='bilinear')
    #     plt.axis('off')
    #     plt.show()

    # Another method to run:
    def run_now(self, output_path: str, **kwargs) -> None:
        """
        Generate a word cloud image.

        :param output_path: The path to the output file.
        """
        WordCloud(**kwargs).generate(self.text).to_file(output_path)


if __name__ == "__main__":
    wordcloud_type = input("Enter fa to create Persian movies Word Cloud, or enter en to create English movies Word Cloud: ")
    if wordcloud_type == 'fa':
        movies_wordcloud = WordCloudGenerator('data/fa_movies.txt', if_rtl=True)  # Specify the path to your Persian movies text file
        movies_wordcloud.run()  # Display the word cloud
        # Uncomment the line below to save the word cloud to a file
        movies_wordcloud.run('output/movies_wordcloud_fa.png')  # Save the word cloud to a file
    else:
        # Default to English movies word cloud
        movies_wordcloud = WordCloudGenerator('data/en_movies.txt')
        movies_wordcloud.run()  # Display the word cloud
        # Uncomment the line below to save the word cloud to a file
        movies_wordcloud.run('output/movies_wordcloud_en.png')  # Save the word cloud to a file

