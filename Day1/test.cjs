let fetch = require("node-fetch");
//"content-type": "application/x-www-form-urlencoded; charset=UTF-8",

let get_data = async () => {
	let res = await fetch("http://127.0.0.1:5000/students");
	if(res.status===200) {
		let data = await res.json();
		console.log(data);
	}
	else {
		console.log("Da,mn!!!! errror");
	}
}

let post_data = async(name, id) => {
	let res = await fetch("http://127.0.0.1:5000/students/new", {
		body: `name=${name}&id=${id}`,
		method: "POST", 
		headers: {
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
		}
	});
	if(res.status===200) {
		let data = await res.json();
		console.log(data);
	}
	else if(res.status===400) {
		console.log("invalid data");
	}
	else {
		console.log("Da,mn!!!! errror");
	}
}

console.log("post run start");
post_data("atif", "5")
.then(()=>{
	console.log("post_run complete");
	get_data();
})
.then(()=>{
	console.log("get complete");
});
