import org.opencv.core.*;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.videoio.VideoCapture;
import org.eclipse.paho.client.mqttv3.*;
import org.bytedeco.javacpp.opencv_core.*;
import org.bytedeco.javacpp.opencv_objdetect.CascadeClassifier;
import org.bytedeco.javacv.*;
import org.bytedeco.dlib.*;
import org.bytedeco.javacpp.dlib.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class DrowsinessDetection {
    static {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME); // Chargement de la bibliothèque OpenCV
    }
    
    // Paramètres MQTT et seuils de détection
    private static final String BROKER_URL = "tcp://localhost:1883";
    private static final String MQTT_TOPIC = "message/prevention";
    private static final double EYE_AR_THRESH = 0.3; // Seuil pour la fermeture des yeux
    private static final int EYE_AR_CONSEC_FRAMES = 30; // Nombre de frames consécutives pour déclencher l'alarme
    private static final int YAWN_THRESH = 20; // Seuil pour le bâillement
    
    private static boolean alarmStatus = false;
    private static boolean alarmStatus2 = false;
    private static int counter = 0;
    private static MqttClient mqttClient;
    
    public static void main(String[] args) throws Exception {
        // Initialisation du client MQTT
        mqttClient = new MqttClient(BROKER_URL, MqttClient.generateClientId());
        mqttClient.connect();
        
        // Ouverture du flux vidéo
        VideoCapture camera = new VideoCapture(0);
        if (!camera.isOpened()) {
            System.out.println("Erreur : Impossible d'ouvrir la caméra");
            return;
        }
        
        Mat frame = new Mat();
        CascadeClassifier faceDetector = new CascadeClassifier("haarcascade_frontalface_default.xml"); // Détection de visage
        ShapePredictor predictor = new ShapePredictor("shape_predictor_68_face_landmarks.dat"); // Prédicteur des points de repère faciaux
        
        while (true) {
            camera.read(frame); // Capture d'une image
            if (frame.empty()) continue;
            
            Mat grayFrame = new Mat();
            Imgproc.cvtColor(frame, grayFrame, Imgproc.COLOR_BGR2GRAY); // Conversion en niveaux de gris
            
            Rect[] faces = detectFaces(faceDetector, grayFrame); // Détection des visages
            for (Rect face : faces) {
                // Prédiction des points du visage
                FullObjectDetection shape = predictor.predict(new Mat(grayFrame), new dlib.rectangle(face.x, face.y, face.x + face.width, face.y + face.height));
                double ear = computeEAR(shape); // Calcul du rapport d'aspect des yeux (EAR)
                double distance = computeLipDistance(shape); // Calcul de la distance des lèvres (bâillement)
                
                // Vérification de la fermeture des yeux
                if (ear < EYE_AR_THRESH) {
                    counter++;
                    if (counter >= EYE_AR_CONSEC_FRAMES && !alarmStatus) {
                        alarmStatus = true;
                        sendMqttMessage("Ne vous endormez pas au volant et faites une pause !|None");
                    }
                } else {
                    counter = 0;
                    alarmStatus = false;
                }
                
                // Vérification du bâillement
                if (distance > YAWN_THRESH && !alarmStatus2) {
                    alarmStatus2 = true;
                    sendMqttMessage("Vous devez faire une pause !|10");
                } else {
                    alarmStatus2 = false;
                }
            }
        }
    }
    
    // Méthode pour détecter les visages dans une image
    private static Rect[] detectFaces(CascadeClassifier detector, Mat image) {
        RectVector detectedFaces = new RectVector();
        detector.detectMultiScale(new Mat(image), detectedFaces);
        Rect[] faces = new Rect[(int) detectedFaces.size()];
        for (int i = 0; i < faces.length; i++) {
            faces[i] = detectedFaces.get(i);
        }
        return faces;
    }
    
    // Méthode pour calculer l'Eye Aspect Ratio (EAR) pour détecter la fermeture des yeux
    private static double computeEAR(FullObjectDetection shape) {
        // Implémentation réelle nécessaire ici
        return Math.random() * 0.5; // Simulation
    }
    
    // Méthode pour calculer la distance entre les lèvres pour détecter le bâillement
    private static double computeLipDistance(FullObjectDetection shape) {
        // Implémentation réelle nécessaire ici
        return Math.random() * 30; // Simulation
    }
    
    // Méthode pour envoyer un message MQTT
    private static void sendMqttMessage(String message) {
        try {
            mqttClient.publish(MQTT_TOPIC, new MqttMessage(message.getBytes()));
            System.out.println("MQTT Message Sent: " + message);
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }
}
