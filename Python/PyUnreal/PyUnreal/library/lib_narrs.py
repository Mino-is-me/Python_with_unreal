
#######################################import modules from here#######################################
import unreal 
#######################################import modules end#######################################



#######################################functions from here#######################################
def get_selected_asset_dir() -> str :
    ar_asset_lists = unreal.EditorUtilityLibrary.get_selected_assets() 

    if len(ar_asset_lists) > 0 :
        str_selected_asset = unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(ar_asset_lists[0])
        path = str_selected_asset.rsplit('/', 1)[0]

    else : 
        path = '' 

    return path


def get_anim_list (__path: str) -> list :
    seq_list = unreal.EditorAssetLibrary.list_assets(__path, True, False)
    return seq_list


def check_animseq_by_name_in_list (__anim_name: str, __list: list ) -> str :
    for each in __list :
        name = each.rsplit('.', 1)[1]
        found_name = name.find(__anim_name)
        if found_name != -1 :
            break 
    return each


def set_bs_sample (__animation, __axis_x: float, __axis_y: float) : # returns [BlendSample] unreal native type 
    bs_sample = unreal.BlendSample()
    vec_sample = unreal.Vector(__axis_x, __axis_y, 0.0) #do not use 3D BlendSampleVector
    bs_sample.set_editor_property('animation', __animation)
    bs_sample.set_editor_property('sample_value', vec_sample)
    bs_sample.set_editor_property('rate_scale', 1.0)
    bs_sample.set_editor_property('snap_to_grid', True)
    return bs_sample



def set_blendSample_to_bs (__blendspace, __blendsample) : #returns [BlendSpace] unreal loaded asset
    __blendspace.set_editor_property('sample_data', __blendsample)
    return 0


def get_bp_c_by_name(__bp_dir:str):
    __bp_c = __bp_dir + '_c' 
    return __bp_c 

def get_bp_mesh_comp_by_name (__bp_c:str, __seek_comp_name:str) :
    #source_mesh = ue.load_asset(__mesh_dir)
    loaded_bp_c = unreal.EditorAssetLibrary.load_blueprint_class(__bp_c)
    bp_c_obj = unreal.get_default_object(loaded_bp_c)
    loaded_comp = bp_c_obj.get_editor_property(__seek_comp_name)
    return loaded_comp

# BP 컴포넌트 접근 순서
## 블루프린트 클래스 로드
### 디폴트 오브젝트 로드
#### 컴포넌트 로드 (get_editor_property)



#######################################functions end#######################################


#######################################class from here######################################

class wrapedBlendSpaceSetting:

   
    bs_dir: str = '/Animation/BlendSpace' #blend space relative path 
    post_fix: str = '' #edit this if variation
    pre_fix: str = '' #edit this if variation
    custom_input: str = pre_fix + '/Animation' + post_fix

    bs_names: list = [
        "IdleRun_BS_Peaceful", 
        "IdleRun_BS_Battle", 
        "Down_BS", 
        "Groggy_BS", 
        "Airborne_BS",
        "LockOn_BS"
        ]

    seq_names: list = [
        '_Idle01',
        '_Walk_L',
        '_BattleIdle01',
        '_Run_L',
        '_KnockDown_L',
        '_Groggy_L',
        '_Airborne_L',
        '_Caution_Cw',
        '_Caution_Fw',
        '_Caution_Bw',
        '_Caution_Lw',
        '_Caution_Rw'
    ]