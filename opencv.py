import com.qualcomm.robotcore.hardwar.HardwareMap;

import org.firstinspires.ftc.robotcore.extrenal.hardware.camera.WebcamName;
import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.Rect;
import org.opencv.core.Scalar;
import org.opencv.imgproc.Imgproc;
import org.openftc.easyopencv.OpenCvCamera;
import org.openftc.easyopencv.OpenCvCameraFactory;
import org.openftc.easyopencv.OpenCvPipeline;

import java.util.ArrayList;
import java.util.List;

public class OpenCV extends EasyOpenCV {

	public static OpenCVCamera camera;
	public int path;

	public enum position {
		LEFT,
		CENTER,
		RIGHT
  }

	public static void init(){
		camera=hardwareMap.get(OpenCVCamera.class, "camera");
    
  }
  
}
