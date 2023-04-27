<script>
	import FaLinkedin from 'svelte-icons/fa/FaLinkedin.svelte';
	import FaGithub from 'svelte-icons/fa/FaGithub.svelte';
	import FaEnvelope from 'svelte-icons/fa/FaEnvelope.svelte';
	import FaMedium from 'svelte-icons/fa/FaMedium.svelte';
	// import { modalOpened } from '$lib/store';
	import { onMount } from 'svelte';

	let text = "";
    let summary = "";
	let error = "";

	async function summarizeText() {
		const url = "http://localhost:5000/summarize";
		const data = { text: text, percentage: 0.5 };
		const options = {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(data),
		};

		try {
		const response = await fetch(url, options);
		const result = await response.json();

		if (response.ok) {
			summary = result.summary;
		} else {
			error = result.error;
		}
		} catch (err) {
		error = err.message;
		}
	}

	
	// let originalTitle;
	// let scrollingTitle;
	// let scrollIndex = 0;

	// function startScrollingTitle() {
	// 	scrollingTitle = setInterval(() => {
	// 	document.title = originalTitle.substring(scrollIndex) + " " + originalTitle.substring(0, scrollIndex);
	// 	scrollIndex++;

	// 	if (scrollIndex > originalTitle.length) {
	// 		scrollIndex = 0;
	// 	}
	// 	}, 700);
	// }

	// function stopScrollingTitle() {
	// 	clearInterval(scrollingTitle);
	// 	document.title = originalTitle;
	// }

	// onMount(() => {
	// 	originalTitle = document.title;
	// 	startScrollingTitle();

	// 	// Stop scrolling when the tab is active and resume when it's inactive
	// 	window.addEventListener("focus", stopScrollingTitle);
	// 	window.addEventListener("blur", startScrollingTitle);

	// 	return () => {
	// 	// Clean up event listeners when the component is destroyed
	// 	window.removeEventListener("focus", stopScrollingTitle);
	// 	window.removeEventListener("blur", startScrollingTitle);
	// 	};
	// });


</script>

<svelte:head>
	<title>Gordon Moore</title>
</svelte:head>
<main>
	<h1>Hi<br /> </h1>
    <h2>Enter the text you would like summarized here!</h2>

    <textarea bind:value="{text}"></textarea>
	<button on:click="{summarizeText}">Summarize</button>

	{#if summary}
		<h2>Summary:</h2>
		<p>{summary}</p>
	{/if}

	{#if error}
		<h2>Error:</h2>
		<p>{error}</p>
	{/if}
</main>

<style>
	@import '../../static/global.css';

	a {
		color: white;
		text-decoration: none;
	}
	main {
		text-align: center;
		padding: 0;
		margin: 0 auto;
		text-align: center;

		display: flex;
		flex-direction: column;
		height: calc(100vh - 80px - 88px);
		justify-content: center;
		align-items: center;
	}

	h1 {
		font-weight: 700;
	}

	main > h1 {
		margin: 50px 10px 0;
		font-size: 36px;
	}

    main > h2 {
        margin: 50px 10px 0;
		font-size: 24px;
    }

	p{
		margin: 20px 0;
		font-size: 18px;
		max-width: 700px;
	}

	textarea {
		width: 100%;
		max-width: 700px;
		height: 150px;
		margin: 20px 0;
		padding: 10px;
		border-radius: 5px;
		border: 1px solid #ccc;
	}

	button{
		background-color: var(--accent-color);
		border: none;
		color: white;
		padding: 15px 32px;
		text-align: center;
		text-decoration: none;
		display: inline-block;
		font-size: 16px;
		border-radius: 5px;
	}

	@media (min-width: 900px) {
		main > h1 {
			font-size: 48px;
		}
	}

	@media (min-width: 600px) {
		main {
			max-width: none;
		}
	}
</style>
