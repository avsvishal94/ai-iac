export default function Upload() {
  const upload = async (file: File) => {
    const form = new FormData();
    form.append("file", file);

    const res = await fetch("http://localhost:8000/generate", {
      method: "POST",
      body: form
    });

    const data = await res.json();
    console.log("Response:", data);
    alert("Upload successful. Check console.");
  };

  return (
    <input
      type="file"
      onChange={(e) => e.target.files && upload(e.target.files[0])}
    />
  );
}
