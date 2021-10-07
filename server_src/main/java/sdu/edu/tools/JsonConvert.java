package sdu.edu.tools;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;

import java.util.ArrayList;
import java.util.Set;

public class JsonConvert {
    public static String[] JsonArraytoString(JSONArray jsonArray){
        ArrayList<String> list = new ArrayList<String>();
        if (jsonArray != null) {
            int len = jsonArray.size();
            for (int i=0;i<len;i++){
                list.add(jsonArray.get(i).toString());
            }
        }
        String[] permission = (String[])list.toArray(new String[jsonArray.size()]);

        return permission;
    }
    public static String [] JsonObjecttoString(JSONObject jsonObject){
        ArrayList<String> list = new ArrayList<String>();
        Set<String> keySet = jsonObject.keySet();
        for(String key:keySet){
            String value = jsonObject.get(key).toString();
            list.add(key+"+"+value);
        }
        return (String[])list.toArray(new String[keySet.size()]);
    }
    public static String ConvertData(double behavior_scores,JSONObject JsonResult){
        int[] array = new int[6];
        int tmp = (int)behavior_scores;
        for(int i =0;i<6;i++){
            array[i] = tmp%10*10;
            tmp /= 10;
            JsonResult.put('a'+String.valueOf((i+1)),array[i]+10);
        }
        return JsonResult.toString();

    }
}
