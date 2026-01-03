import cv2
import numpy as np

def detect_icons(image_bytes):
    """
    Placeholder detector.
    Replace with YOLOv8 later.
    """
    img = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

    return [
        {"id": "vpc-1", "type": "aws_vpc"},
        {"id": "eks-1", "type": "aws_eks"},
        {"id": "alb-1", "type": "aws_alb"}
    ]
