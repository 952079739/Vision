function checkna() {

	na = form.author.value;

	if(na.length < 1 || na.length > 5) {

		divname.innerHTML = '<font class="tips_false">长度是1~5个字符</font>';

	} else {

		divname.innerHTML = '<font class="tips_true">输入正确</font>';

	}

}

function checktle() {

	na = form.title.value;

	if(na.length < 1 || na.length > 20) {

		divpd1.innerHTML = '<font class="tips_false">长度是1~20个字符</font>';

	} else {

		divpd1.innerHTML = '<font class="tips_true">输入正确</font>';

	}

}