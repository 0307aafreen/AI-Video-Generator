// get html elements
const generateBtn = document.getElementById("generateBtn");

const promptInput = document.getElementById("prompt");

const loading = document.getElementById("loading");

const videoPlayer = document.getElementById("videoPlayer");

// button click event
generateBtn.addEventListener("click", async () => {

    // get prompt text
    const prompt = promptInput.value.trim();

    // check empty input
    if (!prompt) {

        alert("Please enter a prompt");

        return;
    }

    console.log("Button clicked");

    // show loading text
    loading.classList.remove("hidden");

    // hide previous video
    videoPlayer.classList.add("hidden");

    // disable button while processing
    generateBtn.disabled = true;

    // change button text
    generateBtn.innerText = "Generating...";

    try {

        console.log("Sending request to backend...");

        // send request to fastapi backend
        const response = await fetch(

            "http://127.0.0.1:8000/generate-video",

            {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                // send prompt to backend
                body: JSON.stringify({

                    prompt: prompt
                })
            }
        );

        console.log("Response received");

        // convert response to json
        const data = await response.json();

        console.log(data);

        // success response
        if (data.success) {

            console.log("Video generated successfully");

            // prevent old cached video
            videoPlayer.src =
                data.video_url + "?t=" + new Date().getTime();

            // reload video
            videoPlayer.load();

            // show video player
            videoPlayer.classList.remove("hidden");

            // autoplay video
            videoPlayer.play();

        } else {

            console.log("Backend Error:", data.error);

            alert(data.error);
        }

    } catch (error) {

        console.log("Frontend Error:", error);

        alert("Server connection failed");
    }

    // hide loading
    loading.classList.add("hidden");

    // enable button again
    generateBtn.disabled = false;

    // reset button text
    generateBtn.innerText = "Generate Video";
});