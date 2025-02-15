% rebase('base.tpl')

<h2>{{app.name}}</h2>
% if app.operation:
	<script type="text/JavaScript">
		async function reloadWhenDone() {
			url = "/{{ platform }}/progress/" + "{{app.content_id}}";
			response = await fetch(url);
			result = await response.json();
			if (!result.operation) {
				location.reload(true);
			} else {
				if (result.progress != -1) {
					document.getElementById('progress').innerHTML = result.progress + "%";
				}
				setTimeout(reloadWhenDone, 1000);
			}
		}
		reloadWhenDone();
	</script>
	<h3>
		{{app.operation}}... <div id="progress"></div>
	</h3>
% elif app.installed_version:
	<h3>Version: {{app.installed_version}}</h3>
% end
<p>{{app.summary}}</p>

<div class="img-container">
	<img src="{{app.image_url}}" alt="{{ app.name }}" title="{{ app.name }}">
</div>

% if not app.operation:
	% if app.installed:
		% if app.installed_version != app.available_version:
			<form action="/{{platform}}/update/{{app.content_id}}">
				<button class="add">Update to version {{app.available_version}}</button>
			</form>
		% end
		<form action="/{{platform}}/uninstall/{{app.content_id}}">
			<button class="delete">Uninstall</button>
		</form>
	% else:
		<form action="/{{ platform }}/install/{{app.content_id}}">
			<button class="add">Install</button>
		</form>
	% end
% end
