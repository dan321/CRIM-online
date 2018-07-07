from django.shortcuts import render
from crim.helpers.solrsearch import CRIMSolrSearch


def search(request):
    if 'q' not in request.GET:
        return _empty_search(request)
    else:
        return render(request, 'search/results.html')


def _empty_search(request):
    s = CRIMSolrSearch(request)
    ret = s.facets(fq=['crim_relationship'], rows=0)
    facets = ret.facet_counts['facet_fields']

    data = {
        'observer': facets['observer_s'],
        'rt_q': facets['rt_q_b'],
        'rt_q_x': facets['rt_q_x_b'],
        'rt_q_monnayage': facets['rt_q_monnayage_b'],
        'rt_tm': facets['rt_tm_b'],
        'rt_tm_snd': facets['rt_tm_snd_b'],
        'rt_tm_minv': facets['rt_tm_minv_b'],
        'rt_tm_retrograde': facets['rt_tm_retrograde_b'],
        'rt_tm_ms': facets['rt_tm_ms_b'],
        'rt_tm_transposed': facets['rt_tm_transposed_b'],
        'rt_tm_invertible': facets['rt_tm_invertible_b'],
        'rt_tnm': facets['rt_tnm_b'],
        'rt_tnm_embellished': facets['rt_tnm_embellished_b'],
        'rt_tnm_reduced': facets['rt_tnm_reduced_b'],
        'rt_tnm_amplified': facets['rt_tnm_amplified_b'],
        'rt_tnm_truncated': facets['rt_tnm_truncated_b'],
        'rt_tnm_ncs': facets['rt_tnm_ncs_b'],
        'rt_tnm_ocs': facets['rt_tnm_ocs_b'],
        'rt_tnm_ocst': facets['rt_tnm_ocst_b'],
        'rt_tnm_nc': facets['rt_tnm_nc_b'],
        'rt_nm': facets['rt_nm_b'],
        'rt_om': facets['rt_om_b'],
        'remarks': facets['remarks_t'],
        'created': facets['created_dt'],
        'updated': facets['updated_dt'],
        'status': facets['status_b'],
        'model_observer': facets['model_observer_s'],
        'model_ema': facets['model_ema_t'],
        'model_mt_cf': facets['model_mt_cf_b'],
        'model_mt_cf_voices': facets['model_mt_cf_voices_ss'],
        'model_mt_cf_dur': facets['model_mt_cf_dur_b'],
        'model_mt_cf_mel': facets['model_mt_cf_mel_b'],
        'model_mt_sog': facets['model_mt_sog_b'],
        'model_mt_sog_voices': facets['model_mt_sog_voices_ss'],
        'model_mt_sog_dur': facets['model_mt_sog_dur_b'],
        'model_mt_sog_mel': facets['model_mt_sog_mel_b'],
        'model_mt_sog_ostinato': facets['model_mt_sog_ostinato_b'],
        'model_mt_sog_periodic': facets['model_mt_sog_periodic_b'],
        'model_mt_csog': facets['model_mt_csog_b'],
        'model_mt_csog_voices': facets['model_mt_csog_voices_ss'],
        'model_mt_csog_dur': facets['model_mt_csog_dur_b'],
        'model_mt_csog_mel': facets['model_mt_csog_mel_b'],
        'model_mt_cd': facets['model_mt_cd_b'],
        'model_mt_cd_voices': facets['model_mt_cd_voices_ss'],
        'model_mt_fg': facets['model_mt_fg_b'],
        'model_mt_fg_voices': facets['model_mt_fg_voices_ss'],
        'model_mt_fg_periodic': facets['model_mt_fg_periodic_b'],
        'model_mt_fg_strict': facets['model_mt_fg_strict_b'],
        'model_mt_fg_flexed': facets['model_mt_fg_flexed_b'],
        'model_mt_fg_sequential': facets['model_mt_fg_sequential_b'],
        'model_mt_fg_inverted': facets['model_mt_fg_inverted_b'],
        'model_mt_fg_retrograde': facets['model_mt_fg_retrograde_b'],
        'model_mt_fg_int': facets['model_mt_fg_int_s'],
        'model_mt_fg_tint': facets['model_mt_fg_tint_s'],
        'model_mt_pe': facets['model_mt_pe_b'],
        'model_mt_pe_voices': facets['model_mt_pe_voices_ss'],
        'model_mt_pe_strict': facets['model_mt_pe_strict_b'],
        'model_mt_pe_flexed': facets['model_mt_pe_flexed_b'],
        'model_mt_pe_flt': facets['model_mt_pe_flt_b'],
        'model_mt_pe_sequential': facets['model_mt_pe_sequential_b'],
        'model_mt_pe_added': facets['model_mt_pe_added_b'],
        'model_mt_pe_invertible': facets['model_mt_pe_invertible_b'],
        'model_mt_pe_int': facets['model_mt_pe_int_s'],
        'model_mt_pe_tint': facets['model_mt_pe_tint_s'],
        'model_mt_id': facets['model_mt_id_b'],
        'model_mt_id_voices': facets['model_mt_id_voices_ss'],
        'model_mt_id_strict': facets['model_mt_id_strict_b'],
        'model_mt_id_flexed': facets['model_mt_id_flexed_b'],
        'model_mt_id_flt': facets['model_mt_id_flt_b'],
        'model_mt_id_invertible': facets['model_mt_id_invertible_b'],
        'model_mt_id_int': facets['model_mt_id_int_s'],
        'model_mt_id_tint': facets['model_mt_id_tint_s'],
        'model_mt_nid': facets['model_mt_nid_b'],
        'model_mt_nid_voices': facets['model_mt_nid_voices_ss'],
        'model_mt_nid_strict': facets['model_mt_nid_strict_b'],
        'model_mt_nid_flexed': facets['model_mt_nid_flexed_b'],
        'model_mt_nid_flt': facets['model_mt_nid_flt_b'],
        'model_mt_nid_sequential': facets['model_mt_nid_sequential_b'],
        'model_mt_nid_invertible': facets['model_mt_nid_invertible_b'],
        'model_mt_nid_int': facets['model_mt_nid_int_s'],
        'model_mt_nid_tint': facets['model_mt_nid_tint_s'],
        'model_mt_hr': facets['model_mt_hr_b'],
        'model_mt_hr_voices': facets['model_mt_hr_voices_ss'],
        'model_mt_hr_simple': facets['model_mt_hr_simple_b'],
        'model_mt_hr_staggered': facets['model_mt_hr_staggered_b'],
        'model_mt_hr_sequential': facets['model_mt_hr_sequential_b'],
        'model_mt_hr_fauxbourdon': facets['model_mt_hr_fauxbourdon_b'],
        'model_mt_cad': facets['model_mt_cad_b'],
        'model_mt_cad_cantizans': facets['model_mt_cad_cantizans_s'],
        'model_mt_cad_tenorizans': facets['model_mt_cad_tenorizans_s'],
        'model_mt_cad_type': facets['model_mt_cad_type_s'],
        'model_mt_cad_tone': facets['model_mt_cad_tone_s'],
        'model_mt_cad_dtv': facets['model_mt_cad_dtv_s'],
        'model_mt_cad_dti': facets['model_mt_cad_dti_s'],
        'model_mt_int': facets['model_mt_int_b'],
        'model_mt_int_voices': facets['model_mt_int_voices_ss'],
        'model_mt_int_p6': facets['model_mt_int_p6_b'],
        'model_mt_int_p3': facets['model_mt_int_p3_b'],
        'model_mt_int_c35': facets['model_mt_int_c35_b'],
        'model_mt_int_c83': facets['model_mt_int_c83_b'],
        'model_mt_int_c65': facets['model_mt_int_c65_b'],
        'model_mt_fp': facets['model_mt_fp_b'],
        'model_mt_fp_comment': facets['model_mt_fp_comment_t'],
        'model_mt_fp_ir': facets['model_mt_fp_ir_b'],
        'model_mt_fp_range': facets['model_mt_fp_range_s'],
        'model_remarks': facets['model_remarks_t'],
        'model_created': facets['model_created_dt'],
        'model_updated': facets['model_updated_dt'],
        'model_status': facets['model_status_b'],
        'model_piece_id': facets['model_piece_id_s'],
        'model_title': facets['model_title_s'],
        'model_mass': facets['model_mass_s'],
        'model_composer': facets['model_composer_s'],
        'model_genre': facets['model_genre_s'],
        'model_date': facets['model_date_i'],
        'model_pdf_links': facets['model_pdf_links_ss'],
        'model_mei_links': facets['model_mei_links_ss'],
        'model_remarks': facets['model_remarks_t'],
        'derivative_observer': facets['derivative_observer_s'],
        'derivative_ema': facets['derivative_ema_t'],
        'derivative_mt_cf': facets['derivative_mt_cf_b'],
        'derivative_mt_cf_voices': facets['derivative_mt_cf_voices_ss'],
        'derivative_mt_cf_dur': facets['derivative_mt_cf_dur_b'],
        'derivative_mt_cf_mel': facets['derivative_mt_cf_mel_b'],
        'derivative_mt_sog': facets['derivative_mt_sog_b'],
        'derivative_mt_sog_voices': facets['derivative_mt_sog_voices_ss'],
        'derivative_mt_sog_dur': facets['derivative_mt_sog_dur_b'],
        'derivative_mt_sog_mel': facets['derivative_mt_sog_mel_b'],
        'derivative_mt_sog_ostinato': facets['derivative_mt_sog_ostinato_b'],
        'derivative_mt_sog_periodic': facets['derivative_mt_sog_periodic_b'],
        'derivative_mt_csog': facets['derivative_mt_csog_b'],
        'derivative_mt_csog_voices': facets['derivative_mt_csog_voices_ss'],
        'derivative_mt_csog_dur': facets['derivative_mt_csog_dur_b'],
        'derivative_mt_csog_mel': facets['derivative_mt_csog_mel_b'],
        'derivative_mt_cd': facets['derivative_mt_cd_b'],
        'derivative_mt_cd_voices': facets['derivative_mt_cd_voices_ss'],
        'derivative_mt_fg': facets['derivative_mt_fg_b'],
        'derivative_mt_fg_voices': facets['derivative_mt_fg_voices_ss'],
        'derivative_mt_fg_periodic': facets['derivative_mt_fg_periodic_b'],
        'derivative_mt_fg_strict': facets['derivative_mt_fg_strict_b'],
        'derivative_mt_fg_flexed': facets['derivative_mt_fg_flexed_b'],
        'derivative_mt_fg_sequential': facets['derivative_mt_fg_sequential_b'],
        'derivative_mt_fg_inverted': facets['derivative_mt_fg_inverted_b'],
        'derivative_mt_fg_retrograde': facets['derivative_mt_fg_retrograde_b'],
        'derivative_mt_fg_int': facets['derivative_mt_fg_int_s'],
        'derivative_mt_fg_tint': facets['derivative_mt_fg_tint_s'],
        'derivative_mt_pe': facets['derivative_mt_pe_b'],
        'derivative_mt_pe_voices': facets['derivative_mt_pe_voices_ss'],
        'derivative_mt_pe_strict': facets['derivative_mt_pe_strict_b'],
        'derivative_mt_pe_flexed': facets['derivative_mt_pe_flexed_b'],
        'derivative_mt_pe_flt': facets['derivative_mt_pe_flt_b'],
        'derivative_mt_pe_sequential': facets['derivative_mt_pe_sequential_b'],
        'derivative_mt_pe_added': facets['derivative_mt_pe_added_b'],
        'derivative_mt_pe_invertible': facets['derivative_mt_pe_invertible_b'],
        'derivative_mt_pe_int': facets['derivative_mt_pe_int_s'],
        'derivative_mt_pe_tint': facets['derivative_mt_pe_tint_s'],
        'derivative_mt_id': facets['derivative_mt_id_b'],
        'derivative_mt_id_voices': facets['derivative_mt_id_voices_ss'],
        'derivative_mt_id_strict': facets['derivative_mt_id_strict_b'],
        'derivative_mt_id_flexed': facets['derivative_mt_id_flexed_b'],
        'derivative_mt_id_flt': facets['derivative_mt_id_flt_b'],
        'derivative_mt_id_invertible': facets['derivative_mt_id_invertible_b'],
        'derivative_mt_id_int': facets['derivative_mt_id_int_s'],
        'derivative_mt_id_tint': facets['derivative_mt_id_tint_s'],
        'derivative_mt_nid': facets['derivative_mt_nid_b'],
        'derivative_mt_nid_voices': facets['derivative_mt_nid_voices_ss'],
        'derivative_mt_nid_strict': facets['derivative_mt_nid_strict_b'],
        'derivative_mt_nid_flexed': facets['derivative_mt_nid_flexed_b'],
        'derivative_mt_nid_flt': facets['derivative_mt_nid_flt_b'],
        'derivative_mt_nid_sequential': facets['derivative_mt_nid_sequential_b'],
        'derivative_mt_nid_invertible': facets['derivative_mt_nid_invertible_b'],
        'derivative_mt_nid_int': facets['derivative_mt_nid_int_s'],
        'derivative_mt_nid_tint': facets['derivative_mt_nid_tint_s'],
        'derivative_mt_hr': facets['derivative_mt_hr_b'],
        'derivative_mt_hr_voices': facets['derivative_mt_hr_voices_ss'],
        'derivative_mt_hr_simple': facets['derivative_mt_hr_simple_b'],
        'derivative_mt_hr_staggered': facets['derivative_mt_hr_staggered_b'],
        'derivative_mt_hr_sequential': facets['derivative_mt_hr_sequential_b'],
        'derivative_mt_hr_fauxbourdon': facets['derivative_mt_hr_fauxbourdon_b'],
        'derivative_mt_cad': facets['derivative_mt_cad_b'],
        'derivative_mt_cad_cantizans': facets['derivative_mt_cad_cantizans_s'],
        'derivative_mt_cad_tenorizans': facets['derivative_mt_cad_tenorizans_s'],
        'derivative_mt_cad_type': facets['derivative_mt_cad_type_s'],
        'derivative_mt_cad_tone': facets['derivative_mt_cad_tone_s'],
        'derivative_mt_cad_dtv': facets['derivative_mt_cad_dtv_s'],
        'derivative_mt_cad_dti': facets['derivative_mt_cad_dti_s'],
        'derivative_mt_int': facets['derivative_mt_int_b'],
        'derivative_mt_int_voices': facets['derivative_mt_int_voices_ss'],
        'derivative_mt_int_p6': facets['derivative_mt_int_p6_b'],
        'derivative_mt_int_p3': facets['derivative_mt_int_p3_b'],
        'derivative_mt_int_c35': facets['derivative_mt_int_c35_b'],
        'derivative_mt_int_c83': facets['derivative_mt_int_c83_b'],
        'derivative_mt_int_c65': facets['derivative_mt_int_c65_b'],
        'derivative_mt_fp': facets['derivative_mt_fp_b'],
        'derivative_mt_fp_comment': facets['derivative_mt_fp_comment_t'],
        'derivative_mt_fp_ir': facets['derivative_mt_fp_ir_b'],
        'derivative_mt_fp_range': facets['derivative_mt_fp_range_s'],
        'derivative_remarks': facets['derivative_remarks_t'],
        'derivative_created': facets['derivative_created_dt'],
        'derivative_updated': facets['derivative_updated_dt'],
        'derivative_status': facets['derivative_status_b'],
        'derivative_piece_id': facets['derivative_piece_id_s'],
        'derivative_title': facets['derivative_title_s'],
        'derivative_mass': facets['derivative_mass_s'],
        'derivative_composer': facets['derivative_composer_s'],
        'derivative_genre': facets['derivative_genre_s'],
        'derivative_date': facets['derivative_date_i'],
        'derivative_pdf_links': facets['derivative_pdf_links_ss'],
        'derivative_mei_links': facets['derivative_mei_links_ss'],
        'derivative_remarks': facets['derivative_remarks_t'],
    }
    return render(request, 'search/search.html', data)
