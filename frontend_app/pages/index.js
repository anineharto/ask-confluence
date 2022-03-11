import Head from "next/head";
import { useState } from "react";
import styles from "./index.module.css";
import PropagateLoader from "react-spinners/PropagateLoader";

export default function Home() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState();
  const [loading, setLoading] = useState(false);
  const [color, setColor] = useState("#c6e9fe");
  const style = { position: "fixed", top: "58%", left: "49%"};

  async function onSubmit(event) {
    event.preventDefault();
    fetch(`http://127.0.0.1:8000/askConfluence?question=${question}`, {
      method: "POST",
      credentials: "include",
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    })
    .then(function(response) {
      if (response.status !== 200) {
        console.log(`Looks like there was a problem. Status code: ${response.status}`);
        return;
      }
      response.json().then(function(data) {
        console.log(data);
        setAnswer(data.answer);
        setQuestion("");
        setLoading(false)
      });
    })
    .catch(function(error) {
      console.log("Fetch error: " + error);
    });
  }

  return (
    <div>
      <Head>
        <title>Ask Confluence</title>
        <link rel="icon" href="/conversation.png" />
      </Head>

      <main className={styles.main}>
        <img src="/conversation.png" className={styles.icon} />
        <h3>Ask Confluence</h3>
        <p> Sometimes it can be difficult finding what you're looking for in Confluence.
            If you have a specific question, you can instead ask our AI bot!
        </p>
        <form onSubmit={onSubmit}>
          <input
            type="text"
            name="question"
            placeholder="Enter a question"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <div className="bounce-loading" style={style}>
            <PropagateLoader color={color} loading={loading} size={20} />
          </div>
          <input type="submit" value="Get answer"
            onClick={() => setLoading(!loading)}
          />
        </form>
        <div className={styles.result}>{answer}</div>
      </main>
    </div>
  );
}
