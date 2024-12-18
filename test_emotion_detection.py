from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am glad this happened')
        result_1_dominant_emotion = result_1['dominant_emotion']
        self.assertEqual(result_1_dominant_emotion, 'joy')

        result_2 = emotion_detector('I am really mad about this')
        result_2_dominant_emotion = result_2['dominant_emotion']
        self.assertEqual(result_2_dominant_emotion, 'anger')

        result_3 = emotion_detector('I feel disgusted just hearing about this')
        result_3_dominant_emotion = result_3['dominant_emotion']
        self.assertEqual(result_3_dominant_emotion, 'disgust')

        result_4 = emotion_detector('I am so sad about this')
        result_4_dominant_emotion = result_4['dominant_emotion']
        self.assertEqual(result_4_dominant_emotion, 'sadness')

        result_5 = emotion_detector('I am really afraid that this will happen')
        result_5_dominant_emotion = result_5['dominant_emotion']
        self.assertEqual(result_5_dominant_emotion, 'fear')


unittest.main()