<script>
	// import Navbar from '$lib/components/NavBar.svelte';
	// import Button from '$lib/components/Button.svelte';
	// import FaCopy from 'svelte-icons/fa/FaCopy.svelte';
	// import Tooltip from '$lib/components/Tooltip.svelte';
	// import CopyClipBoard from '$lib/components/CopyToClipBoard.svelte';
	// import { beforeNavigate } from '$app/navigation';

	import { page } from '$app/stores';
	// import Modal from '$lib/components/Modal.svelte';
	import { onMount } from 'svelte';
	// import { customBackground } from '$lib/store';
	// import routes from '$lib/NavRoutes';

	let copied = false;
	let email = 'gjmoore13@gmail.com';
	const cookieEnabled = false;
	$: showCookieModal = false;

</script>

<slot />

<footer>
	 @ 2023 <a class="me" href="https://www.gordonm.day">Gordon Moore</a>
</footer>

<style>
	@import '../../static/global.css';

	* {
		box-sizing: border-box;
	}

	@font-face {
		font-family: 'Fira Code', monospace;
		font-display: optional;
		src: url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;500;600;700&display=swap');
	}

	:global(#svelte) {
		width: 100vw;
		height: 100%;
		max-width: 900px;

		display: flex;
		flex-direction: column;
		justify-content: space-between;
	}

	:global(html),
	:global(body) {
		transition: background-color 0.2s ease 0s;
		position: relative;
		width: 100%;
		height: 100%;
		overflow: auto;
		font-family: 'Fira Code', monospace;
		background-color: var(--background-color);
	}

	:global(body) {
		background-color: var(--background-color);
		background-size: 200% 200%;
		color: white;
		margin: 0;
		box-sizing: border-box;
		display: grid;
		line-height: 1.75;
		place-items: center;
		height: 100%;
		overflow-x: hidden;
	}

	:global(h1) {
		border: 0;
	}

	:global(::selection) {
		color: white;
		background: var(--accent-color); 
		/* #ca3c25 */
	}

	:global(::-webkit-scrollbar) {
		width: 8px;
		height: 8px;
		border-radius: 1px;
	}

	:global(::-webkit-scrollbar-thumb) {
		background-color: #fafffd;
		border-radius: 3px;
	}

	:global(::-webkit-scrollbar-track) {
		background-color: transparent;
		border-radius: 1px;
	}

	@media (min-width: 900px) {
		:global(body) {
			padding: 0 100px;
		}
	}

	:global(a) {
		text-decoration: none;
	}

	:global(a) {
		text-decoration: none;
	}

	a {
		color: rgb(0, 100, 200);
		text-decoration: none;
	}

	a:hover {
		text-decoration: underline;
	}

	a:visited {
		color: rgb(0, 80, 160);
	}

	.modalContainer div {
		display: flex;
		margin-bottom: 20px;
	}

	.modalContainer p {
		margin: 0;
	}

	:global(.tooltip) {
		visibility: hidden;
	}

	.cookieContainer {
		background: white;
		border-radius: 0px;
		text-align: center;
		width: 100%;
		height: 30px;
		color: black;
		padding: 30px;
		display: flex;
		justify-content: space-evenly;
		align-items: center;
		position: fixed;
		bottom: 0px;
		left: 0;
		right: 0;
		margin-left: auto;
		margin-right: auto;
	}
	.cookieContainer > p > a {
		text-decoration: underline;
	}

	.cookieContainer > div {
		cursor: pointer;
	}

	footer {
		font-size: 12px;
		font-weight: 400;
		padding: 30px 0;
		max-width: 900px;
		text-align: center;
		width: 100%;
	}

	footer a {
		text-decoration: none;
		color: #4158d0;
	}
	footer .svelte {
		color: var(--accent-color);
	}

	footer .me {
		color: var(--accent-color);
	}

	@media (min-width: 900px) {
		:global(.tooltip) {
			visibility: visible;
		}
	}
	@media (min-width: 600px) {
		.cookieContainer {
			background: white;
			border-radius: 50px;
			text-align: center;
			width: 350px;
			height: 30px;
			color: black;
			padding: 0 10px;
			display: flex;
			justify-content: space-evenly;
			align-items: center;
			position: fixed;
			bottom: 50px;
			left: 0;
			right: 0;
			margin-left: auto;
			margin-right: auto;
		}
	}
</style>
