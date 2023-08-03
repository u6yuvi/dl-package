"use client"
import { useState } from 'react'

export default function Home() {
  const [inputImage, setInputImage] = useState<File>();
  const [inputText, setInputText] = useState("");
  const [response, setResponse] = useState("");
  return (
    <main className="flex min-h-screen flex-col p-24">
      <h1>CLIPService</h1>
      <input type="text" className="text-black" onChange={(e) => {
        setInputText(e.target.value)
      }} />
      <input type="file" accept="image/png, image/jpeg" onChange={(e) => {
        if (!e.target.files) return;
        if (e.target?.files?.length > 0) {
          console.log(e.target.files)
          setInputImage(e.target.files[0])
        }
      }} />
      <button onClick={() => {
        if (!inputImage || !inputText) return;

        let formdata = new FormData();
        formdata.append("file", inputImage, inputImage?.name);

        fetch(`https://80-u6yuvi-dlpackage-fzjo9gefb6i.ws-us102.gitpod.io/file?text=${inputText}`, {
          method: 'POST',
          body: formdata,
          redirect: 'follow'
        })
          .then((response) => response.text())
          .then((result) => {
            setResponse(result);
          })
          .catch((error) => console.log("error", error));
      }}>submit</button>
      {response}
    </main>
  )
}