"""
Unit test for emotion_detection module.
Tests the emotion_detector function with joy, anger, disgust, sadness, and fear imputs.
"""

import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion_detector funtion"""

    def test_emotion_detector(self):
        """Test sentiment analysis with joy, anger, disgust, sadness, and fear texts"""

        #Test case for joy emotion
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1["dominant_emotion"], "joy")
        self.assertIsNotNone(result_1['joy'])

        #Test case for anger emotion
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2["dominant_emotion"], "anger")
        self.assertIsNotNone(result_2['anger'])

        #Test case for disgust emotion
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3["dominant_emotion"], "disgust")
        self.assertIsNotNone(result_3['disgust'])

        #Test case for sadness emotion
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4["dominant_emotion"], "sadness")
        self.assertIsNotNone(result_4['sadness'])

        #Test case for fear emotion
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5["dominant_emotion"], "fear")
        self.assertIsNotNone(result_5['fear'])


if __name__ == '__main__':
    unittest.main()
