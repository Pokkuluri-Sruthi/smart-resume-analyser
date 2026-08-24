const fileInput = document.querySelector(
    'input[type="file"]'
);

if (fileInput) {

    fileInput.addEventListener("change", function () {

        if (this.files.length > 0) {

            const file = this.files[0];

            const allowedTypes = [
                "application/pdf",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            ];

            if (!allowedTypes.includes(file.type)) {

                alert(
                    "Please upload a PDF or DOCX file."
                );

                this.value = "";
            }

        }

    });

}


const form = document.querySelector("form");

if (form) {

    form.addEventListener("submit", function () {

        const button = form.querySelector("button");

        if (button) {

            button.innerText = "Analyzing...";

            button.disabled = true;

        }

    });

}