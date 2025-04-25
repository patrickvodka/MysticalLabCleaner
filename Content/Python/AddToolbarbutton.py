import unreal

menu_owner = "editorUtilities"
tool_menus = unreal.ToolMenus.get()
owning_menu_name = "LevelEditor.LevelEditorToolBar.AssetsToolBar"

@unreal.uclass()
class createEntry_Example(unreal.ToolMenuEntryScript):
    
    @unreal.ufunction(override=True)
    def execute(self, context):
        asset = unreal.EditorAssetLibrary.load_asset("/Game/_Core/Blueprints/Editor/CustomEditorWidget/EUW_ClearSave")
        unreal.get_editor_subsystem(unreal.EditorUtilitySubsystem).spawn_and_register_tab(asset)
        
    def init_as_toolbar_button(self):
        self.data.menu = owning_menu_name
        self.data.advanced.entry_type = unreal.MultiBlockType.TOOL_BAR_BUTTON
        self.data.icon = unreal.ScriptSlateIcon("EditorStyle", "LevelEditor.Tabs.Details")  # icône fonctionnelle

def Run():    
    entry = createEntry_Example()
    entry.init_as_toolbar_button()
    entry.init_entry(menu_owner, "editorUtilitiesExampleEntry", "", "", "Example Button", "Opens up Editor Menu")
    toolbar = tool_menus.extend_menu(owning_menu_name)
    toolbar.add_menu_entry_object(entry)
    tool_menus.refresh_all_widgets()

Run()
