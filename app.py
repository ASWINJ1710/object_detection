
import streamlit as st
import cv2
import time
from collections import Counter
from detector import ObjectDetector
from classes import OBJECT_CATEGORIES


# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Live Object Detection",
    page_icon="🎯",
    layout="wide"
)


# =====================================
# PROFESSIONAL UI
# =====================================

st.markdown("""
<style>
.stApp {
    background: #10141D;
    color: white;
}

h1, h2, h3, p, label {
    color: white !important;
}

[data-testid="stSidebar"] {
    background: #171E29;
}

[data-testid="stMetric"] {
    background: #202B3A;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #34445A;
}

.stButton button {
    border-radius: 8px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# =====================================
# LOAD YOLO-WORLD
# =====================================

@st.cache_resource
def load_detector():
    return ObjectDetector()


# =====================================
# HEADER
# =====================================

st.title("🎯 Live Object Detection System")

st.markdown(
    "### YOLO-World | OpenCV | Streamlit"
)

st.caption(
    "Real-time object detection with customizable object categories."
)

st.divider()


# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("⚙️ Detection Settings")

category_names = list(OBJECT_CATEGORIES.keys())

selected_categories = st.sidebar.multiselect(
    "Select object categories",
    category_names,
    default=["Animals", "Vehicles"]
)

selected_classes = []

for category in selected_categories:
    selected_classes.extend(OBJECT_CATEGORIES[category])

selected_classes = list(dict.fromkeys(selected_classes))

confidence = st.sidebar.slider(
    "Confidence threshold",
    0.10,
    0.90,
    0.25,
    0.05
)

st.sidebar.write(
    f"Selected categories: {len(selected_categories)}"
)

st.sidebar.write(
    f"Selected prompts: {len(selected_classes)}"
)


# =====================================
# DASHBOARD METRICS
# =====================================

all_classes = list(dict.fromkeys(
    item
    for items in OBJECT_CATEGORIES.values()
    for item in items
))

col1, col2, col3 = st.columns(3)

col1.metric("Categories", len(OBJECT_CATEGORIES))
col2.metric("Unique Prompts", len(all_classes))
col3.metric("Selected Prompts", len(selected_classes))

st.divider()


# =====================================
# CAMERA CONTROLS
# =====================================

st.subheader("📷 Live Webcam Detection")

col_start, col_stop = st.columns(2)

with col_start:
    start_camera = st.button(
        "▶ START CAMERA",
        use_container_width=True
    )

with col_stop:
    stop_camera = st.button(
        "⏹ STOP CAMERA",
        use_container_width=True
    )


# =====================================
# SESSION STATE
# =====================================

if "camera_running" not in st.session_state:
    st.session_state.camera_running = False

if start_camera:
    st.session_state.camera_running = True

if stop_camera:
    st.session_state.camera_running = False


# =====================================
# VIDEO AND STATISTICS AREAS
# =====================================

video_area = st.empty()

stats_area = st.empty()

if not selected_classes:

    st.warning("Select at least one object category.")

elif st.session_state.camera_running:

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        cap = cv2.VideoCapture(0)

    if not cap.isOpened():

        st.error(
            "Cannot access webcam. Close other apps using the camera."
        )

        st.session_state.camera_running = False

    else:

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Load model
        with st.spinner("Loading YOLO-World..."):
            detector = load_detector()

        # Configure prompts once before detection
        detector.classes = selected_classes
        detector.model.set_classes(selected_classes)

        previous_time = time.time()

        fps = 0.0

        try:

            while st.session_state.camera_running:

                ret, frame = cap.read()

                if not ret:
                    st.error("Unable to read webcam frame.")
                    break

                # Object detection
                detector.confidence = confidence

                output, counts, detections = detector.detect(frame)

                # FPS calculation
                current_time = time.time()
                elapsed = current_time - previous_time

                if elapsed > 0:
                    fps = 1.0 / elapsed

                previous_time = current_time

                # Display FPS
                cv2.putText(
                    output,
                    f"FPS: {fps:.1f}",
                    (15, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.65,
                    (0, 255, 255),
                    2
                )

                cv2.putText(
                    output,
                    f"Objects: {len(detections)}",
                    (15, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.65,
                    (0, 255, 255),
                    2
                )

                # Show video
                video_area.image(
                    cv2.cvtColor(output, cv2.COLOR_BGR2RGB),
                    channels="RGB",
                    use_container_width=True
                )

                # Show detection statistics
                with stats_area.container():

                    metric1, metric2 = st.columns(2)

                    metric1.metric(
                        "Detected Objects",
                        len(detections)
                    )

                    metric2.metric(
                        "Processing FPS",
                        f"{fps:.1f}"
                    )

                    if counts:

                        st.write("### Object Counts")

                        for name, count in counts.items():
                            st.write(f"**{name}:** {count}")

                    else:
                        st.info("No objects detected.")

                # Small delay
                time.sleep(0.01)

        finally:

            cap.release()

            video_area.empty()


# =====================================
# FOOTER
# =====================================

else:

    st.info("Click START CAMERA to begin detection.")

st.divider()

st.caption(
    "Live Object Detection System | YOLO-World + OpenCV"
)
